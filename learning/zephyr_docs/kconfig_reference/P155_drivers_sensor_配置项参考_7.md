---
id: learning.zephyr-docs.kconfig-reference.page-155
title: "`drivers/sensor`配置项参考（7/15）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第155章\_`drivers/sensor`配置项参考（7/15）

本章翻译官方 Kconfig 数据库中 `drivers/sensor` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_IIS2DLPC"></a>

## 155.1 `CONFIG_IIS2DLPC`

**提示（Prompt）**：IIS2DLPC I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**说明（Help）**

启用 IIS2DLPC 加速度传感器（Accelerometer Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_IIS2DLPC_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_GPIO if n
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_IIS2DLPC
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dlpc/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dlpc/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_IIS2DLPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_IIS2DLPC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_IIS2DLPC`。

<a id="CONFIG_IIS2DLPC_ACTIVITY"></a>

## 155.2 `CONFIG_IIS2DLPC_ACTIVITY`

**提示（Prompt）**：活动检测（Activity Detection）

**说明（Help）**

启用活动／非活动检测（Activity/Inactivity Detection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2DLPC_TRIGGER && CONFIG_IIS2DLPC && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dlpc/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dlpc/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DLPC I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_IIS2DLPC_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2DLPC_TRIGGER)、[`CONFIG_IIS2DLPC`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2DLPC)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2DLPC_TRIGGER`。

<a id="CONFIG_IIS2DLPC_TAP"></a>

## 155.3 `CONFIG_IIS2DLPC_TAP`

**提示（Prompt）**：单击与双击检测（Tap and Tap-Tap Detection）

**说明（Help）**

启用敲击检测（Tap Detection），包括单击和双击。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2DLPC_TRIGGER && CONFIG_IIS2DLPC && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dlpc/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dlpc/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DLPC I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_IIS2DLPC_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2DLPC_TRIGGER)、[`CONFIG_IIS2DLPC`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2DLPC)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2DLPC_TRIGGER`。

<a id="CONFIG_IIS2DLPC_THREAD_PRIORITY"></a>

## 155.4 `CONFIG_IIS2DLPC_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2DLPC_TRIGGER_OWN_THREAD && CONFIG_IIS2DLPC_TRIGGER && CONFIG_IIS2DLPC && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dlpc/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dlpc/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DLPC I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_IIS2DLPC_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2DLPC_TRIGGER_OWN_THREAD)、[`CONFIG_IIS2DLPC_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2DLPC_TRIGGER)、[`CONFIG_IIS2DLPC`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2DLPC)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2DLPC_TRIGGER`。

<a id="CONFIG_IIS2DLPC_THREAD_STACK_SIZE"></a>

## 155.5 `CONFIG_IIS2DLPC_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2DLPC_TRIGGER_OWN_THREAD && CONFIG_IIS2DLPC_TRIGGER && CONFIG_IIS2DLPC && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dlpc/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dlpc/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DLPC I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_IIS2DLPC_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2DLPC_TRIGGER_OWN_THREAD)、[`CONFIG_IIS2DLPC_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2DLPC_TRIGGER)、[`CONFIG_IIS2DLPC`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2DLPC)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2DLPC_TRIGGER`。

<a id="CONFIG_IIS2DLPC_TRIGGER_GLOBAL_THREAD"></a>

## 155.6 `CONFIG_IIS2DLPC_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_IIS2DLPC_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dlpc/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dlpc/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DLPC I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS2DLPC_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2DLPC_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2DLPC_TRIGGER`。

<a id="CONFIG_IIS2DLPC_TRIGGER_MODE"></a>

## 155.7 `CONFIG_IIS2DLPC_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2DLPC && CONFIG_SENSOR
```

**可选项（Choices）**

```text
CONFIG_IIS2DLPC_TRIGGER_NONE
CONFIG_IIS2DLPC_TRIGGER_GLOBAL_THREAD
CONFIG_IIS2DLPC_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dlpc/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dlpc/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DLPC I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_IIS2DLPC`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2DLPC)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_IIS2DLPC_TRIGGER_NONE`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2DLPC_TRIGGER_NONE)、[`CONFIG_IIS2DLPC_TRIGGER_GLOBAL_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2DLPC_TRIGGER_GLOBAL_THREAD)、[`CONFIG_IIS2DLPC_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2DLPC_TRIGGER_OWN_THREAD)。

<a id="CONFIG_IIS2DLPC_TRIGGER_NONE"></a>

## 155.8 `CONFIG_IIS2DLPC_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IIS2DLPC_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dlpc/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dlpc/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DLPC I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS2DLPC_TRIGGER_MODE`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2DLPC_TRIGGER_MODE)。

<a id="CONFIG_IIS2DLPC_TRIGGER_OWN_THREAD"></a>

## 155.9 `CONFIG_IIS2DLPC_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_IIS2DLPC_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/iis2dlpc/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2dlpc/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2DLPC I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS2DLPC_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2DLPC_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2DLPC_TRIGGER`。

<a id="CONFIG_IIS2ICLX"></a>

## 155.10 `CONFIG_IIS2ICLX`

**提示（Prompt）**：IIS2ICLX I2C/SPI 加速度计芯片（Accelerometer Chip）

**说明（Help）**

启用 IIS2ICLX 加速度传感器（Accelerometer Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_IIS2ICLX_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_GPIO if n
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_IIS2ICLX
```

**定义位置（Location）**：[`drivers/sensor/st/iis2iclx/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2iclx/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_IIS2ICLX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_IIS2ICLX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_IIS2ICLX`。

<a id="CONFIG_IIS2ICLX_ENABLE_TEMP"></a>

## 155.11 `CONFIG_IIS2ICLX_ENABLE_TEMP`

**提示（Prompt）**：温度（Temperature）

**说明（Help）**

启用／禁用温度功能

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2ICLX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/iis2iclx/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2iclx/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2ICLX I2C/SPI 加速度计芯片（Accelerometer Chip）

**配置项引用（Symbol References）**：[`CONFIG_IIS2ICLX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS2ICLX_EXT_HTS221"></a>

## 155.12 `CONFIG_IIS2ICLX_EXT_HTS221`

**提示（Prompt）**：将 HTS221 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2ICLX_SENSORHUB && CONFIG_IIS2ICLX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/iis2iclx/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2iclx/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2ICLX I2C/SPI 加速度计芯片（Accelerometer Chip） → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_IIS2ICLX_SENSORHUB`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX_SENSORHUB)、[`CONFIG_IIS2ICLX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS2ICLX_EXT_IIS2MDC"></a>

## 155.13 `CONFIG_IIS2ICLX_EXT_IIS2MDC`

**提示（Prompt）**：将 IIS2MDC 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2ICLX_SENSORHUB && CONFIG_IIS2ICLX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/iis2iclx/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2iclx/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2ICLX I2C/SPI 加速度计芯片（Accelerometer Chip） → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_IIS2ICLX_SENSORHUB`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX_SENSORHUB)、[`CONFIG_IIS2ICLX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS2ICLX_EXT_LIS2MDL"></a>

## 155.14 `CONFIG_IIS2ICLX_EXT_LIS2MDL`

**提示（Prompt）**：将 LIS2MDL 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2ICLX_SENSORHUB && CONFIG_IIS2ICLX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/iis2iclx/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2iclx/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2ICLX I2C/SPI 加速度计芯片（Accelerometer Chip） → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_IIS2ICLX_SENSORHUB`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX_SENSORHUB)、[`CONFIG_IIS2ICLX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS2ICLX_EXT_LPS22HB"></a>

## 155.15 `CONFIG_IIS2ICLX_EXT_LPS22HB`

**提示（Prompt）**：将 LPS22HB 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2ICLX_SENSORHUB && CONFIG_IIS2ICLX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/iis2iclx/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2iclx/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2ICLX I2C/SPI 加速度计芯片（Accelerometer Chip） → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_IIS2ICLX_SENSORHUB`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX_SENSORHUB)、[`CONFIG_IIS2ICLX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS2ICLX_EXT_LPS22HH"></a>

## 155.16 `CONFIG_IIS2ICLX_EXT_LPS22HH`

**提示（Prompt）**：将 LPS22HH 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2ICLX_SENSORHUB && CONFIG_IIS2ICLX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/iis2iclx/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2iclx/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2ICLX I2C/SPI 加速度计芯片（Accelerometer Chip） → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_IIS2ICLX_SENSORHUB`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX_SENSORHUB)、[`CONFIG_IIS2ICLX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS2ICLX_SENSORHUB"></a>

## 155.17 `CONFIG_IIS2ICLX_SENSORHUB`

**提示（Prompt）**：I2C 传感器集线器（Sensor Hub）功能

**说明（Help）**

启用／禁用内部传感器集线器（Sensor Hub）。最多可启用两个外部传感器；如果启用了两个以上，系统只会枚举首先找到的两个。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2ICLX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/iis2iclx/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2iclx/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2ICLX I2C/SPI 加速度计芯片（Accelerometer Chip）

**配置项引用（Symbol References）**：[`CONFIG_IIS2ICLX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS2ICLX_THREAD_PRIORITY"></a>

## 155.18 `CONFIG_IIS2ICLX_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2ICLX_TRIGGER_OWN_THREAD && CONFIG_IIS2ICLX_TRIGGER && CONFIG_IIS2ICLX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/iis2iclx/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2iclx/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2ICLX I2C/SPI 加速度计芯片（Accelerometer Chip）

**配置项引用（Symbol References）**：[`CONFIG_IIS2ICLX_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX_TRIGGER_OWN_THREAD)、[`CONFIG_IIS2ICLX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2ICLX_TRIGGER)、[`CONFIG_IIS2ICLX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2ICLX_TRIGGER`。

<a id="CONFIG_IIS2ICLX_THREAD_STACK_SIZE"></a>

## 155.19 `CONFIG_IIS2ICLX_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2ICLX_TRIGGER_OWN_THREAD && CONFIG_IIS2ICLX_TRIGGER && CONFIG_IIS2ICLX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/iis2iclx/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2iclx/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2ICLX I2C/SPI 加速度计芯片（Accelerometer Chip）

**配置项引用（Symbol References）**：[`CONFIG_IIS2ICLX_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX_TRIGGER_OWN_THREAD)、[`CONFIG_IIS2ICLX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2ICLX_TRIGGER)、[`CONFIG_IIS2ICLX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2ICLX_TRIGGER`。

<a id="CONFIG_IIS2ICLX_TRIGGER_GLOBAL_THREAD"></a>

## 155.20 `CONFIG_IIS2ICLX_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_IIS2ICLX_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/iis2iclx/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2iclx/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2ICLX I2C/SPI 加速度计芯片（Accelerometer Chip） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS2ICLX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2ICLX_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2ICLX_TRIGGER`。

<a id="CONFIG_IIS2ICLX_TRIGGER_MODE"></a>

## 155.21 `CONFIG_IIS2ICLX_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2ICLX && CONFIG_SENSOR
```

**可选项（Choices）**

```text
CONFIG_IIS2ICLX_TRIGGER_NONE
CONFIG_IIS2ICLX_TRIGGER_GLOBAL_THREAD
CONFIG_IIS2ICLX_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/iis2iclx/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2iclx/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2ICLX I2C/SPI 加速度计芯片（Accelerometer Chip）

**配置项引用（Symbol References）**：[`CONFIG_IIS2ICLX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_IIS2ICLX_TRIGGER_NONE`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX_TRIGGER_NONE)、[`CONFIG_IIS2ICLX_TRIGGER_GLOBAL_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX_TRIGGER_GLOBAL_THREAD)、[`CONFIG_IIS2ICLX_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX_TRIGGER_OWN_THREAD)。

<a id="CONFIG_IIS2ICLX_TRIGGER_NONE"></a>

## 155.22 `CONFIG_IIS2ICLX_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IIS2ICLX_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/iis2iclx/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2iclx/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2ICLX I2C/SPI 加速度计芯片（Accelerometer Chip） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS2ICLX_TRIGGER_MODE`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2ICLX_TRIGGER_MODE)。

<a id="CONFIG_IIS2ICLX_TRIGGER_OWN_THREAD"></a>

## 155.23 `CONFIG_IIS2ICLX_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_IIS2ICLX_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/iis2iclx/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2iclx/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2ICLX I2C/SPI 加速度计芯片（Accelerometer Chip） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS2ICLX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2ICLX_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2ICLX_TRIGGER`。

<a id="CONFIG_IIS2MDC"></a>

## 155.24 `CONFIG_IIS2MDC`

**提示（Prompt）**：IIS2MDC 磁力计（Magnetometer）

**说明（Help）**

启用基于 I2C 的 IIS2MDC 磁力计传感器（Magnetometer Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_IIS2MDC_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_GPIO if n
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_IIS2MDC
```

**定义位置（Location）**：[`drivers/sensor/st/iis2mdc/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2mdc/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_IIS2MDC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_IIS2MDC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_IIS2MDC`。

<a id="CONFIG_IIS2MDC_MAG_ODR_RUNTIME"></a>

## 155.25 `CONFIG_IIS2MDC_MAG_ODR_RUNTIME`

**提示（Prompt）**：在运行时设置磁力计采样频率（ODR），默认值为 10 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2MDC && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/iis2mdc/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2mdc/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2MDC 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_IIS2MDC`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2MDC)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS2MDC_THREAD_PRIORITY"></a>

## 155.26 `CONFIG_IIS2MDC_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2MDC_TRIGGER_OWN_THREAD && CONFIG_IIS2MDC && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/iis2mdc/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2mdc/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2MDC 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_IIS2MDC_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2MDC_TRIGGER_OWN_THREAD)、[`CONFIG_IIS2MDC`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2MDC)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS2MDC_THREAD_STACK_SIZE"></a>

## 155.27 `CONFIG_IIS2MDC_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2MDC_TRIGGER_OWN_THREAD && CONFIG_IIS2MDC && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/iis2mdc/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2mdc/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2MDC 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_IIS2MDC_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2MDC_TRIGGER_OWN_THREAD)、[`CONFIG_IIS2MDC`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2MDC)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS2MDC_TRIGGER_GLOBAL_THREAD"></a>

## 155.28 `CONFIG_IIS2MDC_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_IIS2MDC_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/iis2mdc/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2mdc/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2MDC 磁力计（Magnetometer） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS2MDC_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2MDC_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2MDC_TRIGGER`。

<a id="CONFIG_IIS2MDC_TRIGGER_MODE"></a>

## 155.29 `CONFIG_IIS2MDC_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS2MDC && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_IIS2MDC_TRIGGER_GLOBAL_THREAD
```

**可选项（Choices）**

```text
CONFIG_IIS2MDC_TRIGGER_NONE
CONFIG_IIS2MDC_TRIGGER_GLOBAL_THREAD
CONFIG_IIS2MDC_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/iis2mdc/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2mdc/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2MDC 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_IIS2MDC`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2MDC)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_IIS2MDC_TRIGGER_GLOBAL_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2MDC_TRIGGER_GLOBAL_THREAD)、[`CONFIG_IIS2MDC_TRIGGER_NONE`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2MDC_TRIGGER_NONE)、[`CONFIG_IIS2MDC_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2MDC_TRIGGER_OWN_THREAD)。

<a id="CONFIG_IIS2MDC_TRIGGER_NONE"></a>

## 155.30 `CONFIG_IIS2MDC_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IIS2MDC_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/iis2mdc/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2mdc/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2MDC 磁力计（Magnetometer） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS2MDC_TRIGGER_MODE`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS2MDC_TRIGGER_MODE)。

<a id="CONFIG_IIS2MDC_TRIGGER_OWN_THREAD"></a>

## 155.31 `CONFIG_IIS2MDC_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_IIS2MDC_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/iis2mdc/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis2mdc/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS2MDC 磁力计（Magnetometer） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS2MDC_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS2MDC_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS2MDC_TRIGGER`。

<a id="CONFIG_IIS328DQ"></a>

## 155.32 `CONFIG_IIS328DQ`

**提示（Prompt）**：IIS328DQ I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**说明（Help）**

启用 IIS328DQ 加速度传感器（Accelerometer Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_IIS328DQ_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_GPIO if n || n
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_IIS328DQ
```

**定义位置（Location）**：[`drivers/sensor/st/iis328dq/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis328dq/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_IIS328DQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_IIS328DQ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_IIS328DQ`。

<a id="CONFIG_IIS328DQ_THREAD_PRIORITY"></a>

## 155.33 `CONFIG_IIS328DQ_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS328DQ_TRIGGER_OWN_THREAD && CONFIG_IIS328DQ_TRIGGER && CONFIG_IIS328DQ && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS328DQ I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_IIS328DQ_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS328DQ_TRIGGER_OWN_THREAD)、[`CONFIG_IIS328DQ_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS328DQ_TRIGGER)、[`CONFIG_IIS328DQ`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS328DQ)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS328DQ_TRIGGER`。

<a id="CONFIG_IIS328DQ_THREAD_STACK_SIZE"></a>

## 155.34 `CONFIG_IIS328DQ_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS328DQ_TRIGGER_OWN_THREAD && CONFIG_IIS328DQ_TRIGGER && CONFIG_IIS328DQ && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS328DQ I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_IIS328DQ_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS328DQ_TRIGGER_OWN_THREAD)、[`CONFIG_IIS328DQ_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS328DQ_TRIGGER)、[`CONFIG_IIS328DQ`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS328DQ)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS328DQ_TRIGGER`。

<a id="CONFIG_IIS328DQ_THRESHOLD"></a>

## 155.35 `CONFIG_IIS328DQ_THRESHOLD`

**提示（Prompt）**：阈值检测（Threshold Detection）

**说明（Help）**

启用阈值中断（Threshold Interrupt）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS328DQ_TRIGGER && CONFIG_IIS328DQ && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/iis328dq/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis328dq/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS328DQ I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_IIS328DQ_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS328DQ_TRIGGER)、[`CONFIG_IIS328DQ`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS328DQ)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS328DQ_TRIGGER`。

<a id="CONFIG_IIS328DQ_TRIGGER_GLOBAL_THREAD"></a>

## 155.36 `CONFIG_IIS328DQ_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_IIS328DQ_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_IIS328DQ_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS328DQ I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_IIS328DQ_TRIGGER_MODE`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS328DQ_TRIGGER_MODE)、[`CONFIG_IIS328DQ_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS328DQ_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS328DQ_TRIGGER`。

<a id="CONFIG_IIS328DQ_TRIGGER_MODE"></a>

## 155.37 `CONFIG_IIS328DQ_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定传感器模块使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS328DQ && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_IIS328DQ_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_IIS328DQ_TRIGGER_NONE
CONFIG_IIS328DQ_TRIGGER_GLOBAL_THREAD
CONFIG_IIS328DQ_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS328DQ I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_IIS328DQ`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS328DQ)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_IIS328DQ_TRIGGER_NONE`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS328DQ_TRIGGER_NONE)、[`CONFIG_IIS328DQ_TRIGGER_GLOBAL_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS328DQ_TRIGGER_GLOBAL_THREAD)、[`CONFIG_IIS328DQ_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS328DQ_TRIGGER_OWN_THREAD)。

<a id="CONFIG_IIS328DQ_TRIGGER_NONE"></a>

## 155.38 `CONFIG_IIS328DQ_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IIS328DQ_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS328DQ I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS328DQ_TRIGGER_MODE`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS328DQ_TRIGGER_MODE)。

<a id="CONFIG_IIS328DQ_TRIGGER_OWN_THREAD"></a>

## 155.39 `CONFIG_IIS328DQ_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_IIS328DQ_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_IIS328DQ_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS328DQ I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_IIS328DQ_TRIGGER_MODE`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS328DQ_TRIGGER_MODE)、[`CONFIG_IIS328DQ_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS328DQ_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS328DQ_TRIGGER`。

<a id="CONFIG_IIS3DHHC"></a>

## 155.40 `CONFIG_IIS3DHHC`

**提示（Prompt）**：IIS3DHHC 加速度传感器（Accelerometer Sensor）

**说明（Help）**

启用基于 SPI 的 IIS3DHHC 加速度传感器（Accelerometer Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_IIS3DHHC_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_GPIO if n
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_IIS3DHHC
```

**定义位置（Location）**：[`drivers/sensor/st/iis3dhhc/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis3dhhc/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_IIS3DHHC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_IIS3DHHC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_IIS3DHHC`。

<a id="CONFIG_IIS3DHHC_DRDY_INT1"></a>

## 155.41 `CONFIG_IIS3DHHC_DRDY_INT1`

**提示（Prompt）**：将数据就绪中断（Data Ready Interrupt）路由至 INT1 引脚

**说明（Help）**

选择 Y 将数据就绪中断（Data Ready Interrupt）路由至 INT1 引脚；选择 N 将其路由至 INT2 引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS3DHHC_TRIGGER && CONFIG_IIS3DHHC && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/iis3dhhc/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis3dhhc/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS3DHHC 加速度传感器（Accelerometer Sensor） → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_IIS3DHHC_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS3DHHC_TRIGGER)、[`CONFIG_IIS3DHHC`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DHHC)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS3DHHC_TRIGGER`。

<a id="CONFIG_IIS3DHHC_NORM_MODE"></a>

## 155.42 `CONFIG_IIS3DHHC_NORM_MODE`

**提示（Prompt）**：传感器以 1 kHz 工作

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS3DHHC && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/iis3dhhc/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis3dhhc/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS3DHHC 加速度传感器（Accelerometer Sensor） → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_IIS3DHHC`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DHHC)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS3DHHC_THREAD_PRIORITY"></a>

## 155.43 `CONFIG_IIS3DHHC_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS3DHHC_TRIGGER_OWN_THREAD && CONFIG_IIS3DHHC && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/iis3dhhc/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis3dhhc/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS3DHHC 加速度传感器（Accelerometer Sensor）

**配置项引用（Symbol References）**：[`CONFIG_IIS3DHHC_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DHHC_TRIGGER_OWN_THREAD)、[`CONFIG_IIS3DHHC`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DHHC)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS3DHHC_THREAD_STACK_SIZE"></a>

## 155.44 `CONFIG_IIS3DHHC_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS3DHHC_TRIGGER_OWN_THREAD && CONFIG_IIS3DHHC && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/iis3dhhc/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis3dhhc/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS3DHHC 加速度传感器（Accelerometer Sensor）

**配置项引用（Symbol References）**：[`CONFIG_IIS3DHHC_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DHHC_TRIGGER_OWN_THREAD)、[`CONFIG_IIS3DHHC`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DHHC)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS3DHHC_TRIGGER_GLOBAL_THREAD"></a>

## 155.45 `CONFIG_IIS3DHHC_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_IIS3DHHC_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/iis3dhhc/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis3dhhc/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS3DHHC 加速度传感器（Accelerometer Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS3DHHC_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS3DHHC_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS3DHHC_TRIGGER`。

<a id="CONFIG_IIS3DHHC_TRIGGER_MODE"></a>

## 155.46 `CONFIG_IIS3DHHC_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS3DHHC && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_IIS3DHHC_TRIGGER_GLOBAL_THREAD
```

**可选项（Choices）**

```text
CONFIG_IIS3DHHC_TRIGGER_NONE
CONFIG_IIS3DHHC_TRIGGER_GLOBAL_THREAD
CONFIG_IIS3DHHC_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/iis3dhhc/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis3dhhc/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS3DHHC 加速度传感器（Accelerometer Sensor）

**配置项引用（Symbol References）**：[`CONFIG_IIS3DHHC`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DHHC)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_IIS3DHHC_TRIGGER_GLOBAL_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DHHC_TRIGGER_GLOBAL_THREAD)、[`CONFIG_IIS3DHHC_TRIGGER_NONE`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DHHC_TRIGGER_NONE)、[`CONFIG_IIS3DHHC_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DHHC_TRIGGER_OWN_THREAD)。

<a id="CONFIG_IIS3DHHC_TRIGGER_NONE"></a>

## 155.47 `CONFIG_IIS3DHHC_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IIS3DHHC_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/iis3dhhc/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis3dhhc/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS3DHHC 加速度传感器（Accelerometer Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS3DHHC_TRIGGER_MODE`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DHHC_TRIGGER_MODE)。

<a id="CONFIG_IIS3DHHC_TRIGGER_OWN_THREAD"></a>

## 155.48 `CONFIG_IIS3DHHC_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_IIS3DHHC_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/iis3dhhc/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis3dhhc/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS3DHHC 加速度传感器（Accelerometer Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_IIS3DHHC_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS3DHHC_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS3DHHC_TRIGGER`。

<a id="CONFIG_IIS3DWB"></a>

## 155.49 `CONFIG_IIS3DWB`

**提示（Prompt）**：IIS3DWB 加速度传感器（Accelerometer Sensor）

**说明（Help）**

启用基于 SPI 的 IIS3DWB 加速度传感器（Accelerometer Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_IIS3DWB_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_SPI_RTIO if CONFIG_SENSOR_ASYNC_API
CONFIG_GPIO if n || n
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_IIS3DWB
```

**定义位置（Location）**：[`drivers/sensor/st/iis3dwb/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis3dwb/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_IIS3DWB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_IIS3DWB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_IIS3DWB`。

<a id="CONFIG_IIS3DWB_ENABLE_TEMP"></a>

## 155.50 `CONFIG_IIS3DWB_ENABLE_TEMP`

**提示（Prompt）**：温度（Temperature）

**说明（Help）**

启用／禁用温度传感器（Temperature Sensor）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IIS3DWB && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/iis3dwb/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis3dwb/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS3DWB 加速度传感器（Accelerometer Sensor）

**配置项引用（Symbol References）**：[`CONFIG_IIS3DWB`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DWB)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_IIS3DWB_STREAM"></a>

## 155.51 `CONFIG_IIS3DWB_STREAM`

**提示（Prompt）**：IIS3DWB 数据流式传输（Data Streaming）

**说明（Help）**

使用此配置选项，启用通过实时 I/O（RTIO）子系统流式传输传感器数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RTIO && CONFIG_SENSOR_ASYNC_API && CONFIG_IIS3DWB && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_IIS3DWB_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/iis3dwb/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/iis3dwb/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → IIS3DWB 加速度传感器（Accelerometer Sensor）

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_IIS3DWB`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DWB)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_IIS3DWB_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IIS3DWB_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_IIS3DWB_TRIGGER`。

<a id="CONFIG_INA219"></a>

## 155.52 `CONFIG_INA219`

**提示（Prompt）**：INA219 电流／功率监测器（Current/Power Monitor）

**说明（Help）**

启用 INA219 双向电流／功率监测器（Bidirectional Current/Power Monitor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_INA219_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/ina219/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/ina219/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_INA226"></a>

## 155.53 `CONFIG_INA226`

**提示（Prompt）**：INA226 电流／功率监测器（Current/Power Monitor）

**说明（Help）**

启用 INA226 双向电流／功率监测器（Bidirectional Current/Power Monitor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_INA226_ENABLED && CONFIG_INA2XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_INA2XX_HAS_CHANNEL_BUS_VOLTAGE
CONFIG_INA2XX_HAS_CHANNEL_SHUNT_VOLTAGE
CONFIG_INA2XX_HAS_CHANNEL_CURRENT
CONFIG_INA2XX_HAS_CHANNEL_POWER
```

**定义位置（Location）**：[`drivers/sensor/ti/ina2xx/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/ina2xx/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → INA2XX 电流与功率监测器（Current and Power Monitor）

**配置项引用（Symbol References）**：[`CONFIG_INA2XX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_INA2XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_INA2XX_HAS_CHANNEL_BUS_VOLTAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA2XX_HAS_CHANNEL_BUS_VOLTAGE)、[`CONFIG_INA2XX_HAS_CHANNEL_SHUNT_VOLTAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA2XX_HAS_CHANNEL_SHUNT_VOLTAGE)、[`CONFIG_INA2XX_HAS_CHANNEL_CURRENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA2XX_HAS_CHANNEL_CURRENT)、[`CONFIG_INA2XX_HAS_CHANNEL_POWER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA2XX_HAS_CHANNEL_POWER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_INA2XX_HAS_CHANNEL_BUS_VOLTAGE`、`CONFIG_INA2XX_HAS_CHANNEL_SHUNT_VOLTAGE`、`CONFIG_INA2XX_HAS_CHANNEL_CURRENT`、`CONFIG_INA2XX_HAS_CHANNEL_POWER`。

<a id="CONFIG_INA228"></a>

## 155.54 `CONFIG_INA228`

**提示（Prompt）**：INA228

**说明（Help）**

启用 INA228 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_INA228_ENABLED && CONFIG_INA2XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_INA237
CONFIG_INA2XX_HAS_CHANNEL_ENERGY
CONFIG_INA2XX_HAS_CHANNEL_CHARGE
```

**定义位置（Location）**：[`drivers/sensor/ti/ina2xx/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/ina2xx/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → INA2XX 电流与功率监测器（Current and Power Monitor）

**配置项引用（Symbol References）**：[`CONFIG_INA2XX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_INA2XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_INA237`](P155_drivers_sensor_配置项参考_7.md#CONFIG_INA237)、[`CONFIG_INA2XX_HAS_CHANNEL_ENERGY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA2XX_HAS_CHANNEL_ENERGY)、[`CONFIG_INA2XX_HAS_CHANNEL_CHARGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA2XX_HAS_CHANNEL_CHARGE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_INA2XX_HAS_CHANNEL_ENERGY`、`CONFIG_INA2XX_HAS_CHANNEL_CHARGE`。

<a id="CONFIG_INA230"></a>

## 155.55 `CONFIG_INA230`

**提示（Prompt）**：INA230

**说明（Help）**

启用 INA230/INA231/INA232/INA236 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_INA230_ENABLED || DT_HAS_TI_INA232_ENABLED || DT_HAS_TI_INA236_ENABLED) && CONFIG_INA2XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_INA2XX_HAS_CHANNEL_BUS_VOLTAGE
CONFIG_INA2XX_HAS_CHANNEL_CURRENT
CONFIG_INA2XX_HAS_CHANNEL_POWER
```

**被选择（Selected by）**

```text
CONFIG_INA232
CONFIG_INA236
```

**定义位置（Location）**：[`drivers/sensor/ti/ina2xx/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/ina2xx/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → INA2XX 电流与功率监测器（Current and Power Monitor）

**配置项引用（Symbol References）**：[`CONFIG_INA2XX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_INA2XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_INA2XX_HAS_CHANNEL_BUS_VOLTAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA2XX_HAS_CHANNEL_BUS_VOLTAGE)、[`CONFIG_INA2XX_HAS_CHANNEL_CURRENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA2XX_HAS_CHANNEL_CURRENT)、[`CONFIG_INA2XX_HAS_CHANNEL_POWER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA2XX_HAS_CHANNEL_POWER)、[`CONFIG_INA232`](P155_drivers_sensor_配置项参考_7.md#CONFIG_INA232)、[`CONFIG_INA236`](P155_drivers_sensor_配置项参考_7.md#CONFIG_INA236)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_INA2XX_HAS_CHANNEL_BUS_VOLTAGE`、`CONFIG_INA2XX_HAS_CHANNEL_CURRENT`、`CONFIG_INA2XX_HAS_CHANNEL_POWER`。

<a id="CONFIG_INA230_TRIGGER"></a>

## 155.56 `CONFIG_INA230_TRIGGER`

**提示（Prompt）**：INA230 触发模式（Trigger Mode）

**说明（Help）**

启用通过 GPIO 中断实现的触发模式（Trigger Mode），中断配置到 ALERT 引脚线上。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INA230 && CONFIG_GPIO && (n || n || n) && CONFIG_INA2XX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/ti/ina2xx/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/ina2xx/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → INA2XX 电流与功率监测器（Current and Power Monitor） → INA230

**配置项引用（Symbol References）**：[`CONFIG_INA230`](P155_drivers_sensor_配置项参考_7.md#CONFIG_INA230)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_INA2XX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_INA2XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_INA232"></a>

## 155.57 `CONFIG_INA232`

**提示（Prompt）**：INA232

**说明（Help）**

启用 INA232 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_INA232_ENABLED && CONFIG_INA2XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_INA230
```

**定义位置（Location）**：[`drivers/sensor/ti/ina2xx/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/ina2xx/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → INA2XX 电流与功率监测器（Current and Power Monitor）

**配置项引用（Symbol References）**：[`CONFIG_INA2XX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_INA2XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_INA230`](P155_drivers_sensor_配置项参考_7.md#CONFIG_INA230)。

<a id="CONFIG_INA236"></a>

## 155.58 `CONFIG_INA236`

**提示（Prompt）**：INA236

**说明（Help）**

启用 INA236 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_INA236_ENABLED && CONFIG_INA2XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_INA230
```

**定义位置（Location）**：[`drivers/sensor/ti/ina2xx/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/ina2xx/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → INA2XX 电流与功率监测器（Current and Power Monitor）

**配置项引用（Symbol References）**：[`CONFIG_INA2XX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_INA2XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_INA230`](P155_drivers_sensor_配置项参考_7.md#CONFIG_INA230)。

<a id="CONFIG_INA237"></a>

## 155.59 `CONFIG_INA237`

**提示（Prompt）**：INA237

**说明（Help）**

启用 INA237/INA228 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_INA237_ENABLED || DT_HAS_TI_INA228_ENABLED) && CONFIG_INA2XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_INA2XX_HAS_CHANNEL_BUS_VOLTAGE
CONFIG_INA2XX_HAS_CHANNEL_SHUNT_VOLTAGE
CONFIG_INA2XX_HAS_CHANNEL_CURRENT
CONFIG_INA2XX_HAS_CHANNEL_POWER
CONFIG_INA2XX_HAS_CHANNEL_DIE_TEMP
```

**被选择（Selected by）**

```text
CONFIG_INA228
```

**定义位置（Location）**：[`drivers/sensor/ti/ina2xx/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/ina2xx/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → INA2XX 电流与功率监测器（Current and Power Monitor）

**配置项引用（Symbol References）**：[`CONFIG_INA2XX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_INA2XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_INA2XX_HAS_CHANNEL_BUS_VOLTAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA2XX_HAS_CHANNEL_BUS_VOLTAGE)、[`CONFIG_INA2XX_HAS_CHANNEL_SHUNT_VOLTAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA2XX_HAS_CHANNEL_SHUNT_VOLTAGE)、[`CONFIG_INA2XX_HAS_CHANNEL_CURRENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA2XX_HAS_CHANNEL_CURRENT)、[`CONFIG_INA2XX_HAS_CHANNEL_POWER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA2XX_HAS_CHANNEL_POWER)、[`CONFIG_INA2XX_HAS_CHANNEL_DIE_TEMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INA2XX_HAS_CHANNEL_DIE_TEMP)、[`CONFIG_INA228`](P155_drivers_sensor_配置项参考_7.md#CONFIG_INA228)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_INA2XX_HAS_CHANNEL_BUS_VOLTAGE`、`CONFIG_INA2XX_HAS_CHANNEL_SHUNT_VOLTAGE`、`CONFIG_INA2XX_HAS_CHANNEL_CURRENT`、`CONFIG_INA2XX_HAS_CHANNEL_POWER`、`CONFIG_INA2XX_HAS_CHANNEL_DIE_TEMP`。

<a id="CONFIG_INA2XX"></a>

## 155.60 `CONFIG_INA2XX`

**提示（Prompt）**：INA2XX 电流与功率监测器（Current and Power Monitor）

**说明（Help）**

启用 INA2XX 电流与功率监测器（Current and Power Monitor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_INA226_ENABLED || DT_HAS_TI_INA228_ENABLED || DT_HAS_TI_INA230_ENABLED || DT_HAS_TI_INA232_ENABLED || DT_HAS_TI_INA236_ENABLED || DT_HAS_TI_INA237_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/ina2xx/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/ina2xx/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_INA3221"></a>

## 155.61 `CONFIG_INA3221`

**提示（Prompt）**：INA3221 三通道电流／功率监测器（Triple-Channel Current/Power Monitor）

**说明（Help）**

启用 INA3221 三通道电流／功率监测器（Triple-Channel Current/Power Monitor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_INA3221_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/ina3221/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/ina3221/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_INA7XX"></a>

## 155.62 `CONFIG_INA7XX`

**提示（Prompt）**：INA7xx 电流／功率监测器（Current/Power Monitor）

**说明（Help）**

启用 INA7xx 双向电流／功率监测器（Bidirectional Current/Power Monitor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_INA7XX_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/ina7xx/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/ina7xx/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_ISL29035"></a>

## 155.63 `CONFIG_ISL29035`

**提示（Prompt）**：ISL29035 光照传感器（Light Sensor）

**说明（Help）**

启用 ISL29035 光照传感器（Light Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ISIL_ISL29035_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_ISL29035_INTEGRATION_TIME_105K"></a>

## 155.64 `CONFIG_ISL29035_INTEGRATION_TIME_105K`

**提示（Prompt）**：105 ms

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 积分时间（Integration Time）

<a id="CONFIG_ISL29035_INTEGRATION_TIME_26"></a>

## 155.65 `CONFIG_ISL29035_INTEGRATION_TIME_26`

**提示（Prompt）**：0.0256 ms

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 积分时间（Integration Time）

<a id="CONFIG_ISL29035_INTEGRATION_TIME_410"></a>

## 155.66 `CONFIG_ISL29035_INTEGRATION_TIME_410`

**提示（Prompt）**：0.41 ms

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 积分时间（Integration Time）

<a id="CONFIG_ISL29035_INTEGRATION_TIME_6500"></a>

## 155.67 `CONFIG_ISL29035_INTEGRATION_TIME_6500`

**提示（Prompt）**：6.5 ms

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 积分时间（Integration Time）

<a id="CONFIG_ISL29035_INT_PERSIST_1"></a>

## 155.68 `CONFIG_ISL29035_INT_PERSIST_1`

**提示（Prompt）**：1

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 中断持续周期数（Interrupt Persist Cycles）

<a id="CONFIG_ISL29035_INT_PERSIST_16"></a>

## 155.69 `CONFIG_ISL29035_INT_PERSIST_16`

**提示（Prompt）**：16

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 中断持续周期数（Interrupt Persist Cycles）

<a id="CONFIG_ISL29035_INT_PERSIST_4"></a>

## 155.70 `CONFIG_ISL29035_INT_PERSIST_4`

**提示（Prompt）**：4

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 中断持续周期数（Interrupt Persist Cycles）

<a id="CONFIG_ISL29035_INT_PERSIST_8"></a>

## 155.71 `CONFIG_ISL29035_INT_PERSIST_8`

**提示（Prompt）**：8

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 中断持续周期数（Interrupt Persist Cycles）

<a id="CONFIG_ISL29035_LUX_RANGE_16K"></a>

## 155.72 `CONFIG_ISL29035_LUX_RANGE_16K`

**提示（Prompt）**：16000

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 满量程照度范围（Full Scale Lux Range）

<a id="CONFIG_ISL29035_LUX_RANGE_1K"></a>

## 155.73 `CONFIG_ISL29035_LUX_RANGE_1K`

**提示（Prompt）**：1000

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 满量程照度范围（Full Scale Lux Range）

<a id="CONFIG_ISL29035_LUX_RANGE_4K"></a>

## 155.74 `CONFIG_ISL29035_LUX_RANGE_4K`

**提示（Prompt）**：4000

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 满量程照度范围（Full Scale Lux Range）

<a id="CONFIG_ISL29035_LUX_RANGE_64K"></a>

## 155.75 `CONFIG_ISL29035_LUX_RANGE_64K`

**提示（Prompt）**：64000

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 满量程照度范围（Full Scale Lux Range）

<a id="CONFIG_ISL29035_MODE_ALS"></a>

## 155.76 `CONFIG_ISL29035_MODE_ALS`

**提示（Prompt）**：环境光（Ambient Light）

**说明（Help）**

环境光光谱的感测模式（Sensing Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 当前感测模式（Active Sensing Mode）

<a id="CONFIG_ISL29035_MODE_IR"></a>

## 155.77 `CONFIG_ISL29035_MODE_IR`

**提示（Prompt）**：红外（Infrared）

**说明（Help）**

红外光谱的感测模式（Sensing Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 当前感测模式（Active Sensing Mode）

<a id="CONFIG_ISL29035_THREAD_PRIORITY"></a>

## 155.78 `CONFIG_ISL29035_THREAD_PRIORITY`

原库同名定义共 2 条；本项为数据库第 8721 条记录，各定义分别保留。

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

用于处理定时器触发和阈值触发的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISL29035 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_ISL29035`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISL29035)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ISL29035_THREAD_PRIORITY--record-8722"></a>

## 155.79 `CONFIG_ISL29035_THREAD_PRIORITY`

原库同名定义共 2 条；本项为数据库第 8722 条记录，各定义分别保留。

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISL29035_TRIGGER_OWN_THREAD && CONFIG_ISL29035 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_ISL29035_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISL29035_TRIGGER_OWN_THREAD)、[`CONFIG_ISL29035`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISL29035)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ISL29035_THREAD_STACK_SIZE"></a>

## 155.80 `CONFIG_ISL29035_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISL29035_TRIGGER_OWN_THREAD && CONFIG_ISL29035 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_ISL29035_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISL29035_TRIGGER_OWN_THREAD)、[`CONFIG_ISL29035`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISL29035)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ISL29035_TRIGGER_GLOBAL_THREAD"></a>

## 155.81 `CONFIG_ISL29035_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ISL29035_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ISL29035_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ISL29035_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ISL29035_TRIGGER`。

<a id="CONFIG_ISL29035_TRIGGER_NONE"></a>

## 155.82 `CONFIG_ISL29035_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 触发模式（Trigger Mode）

<a id="CONFIG_ISL29035_TRIGGER_OWN_THREAD"></a>

## 155.83 `CONFIG_ISL29035_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ISL29035_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/renesas/isl29035/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/renesas/isl29035/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISL29035 光照传感器（Light Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ISL29035_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ISL29035_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ISL29035_TRIGGER`。

<a id="CONFIG_ISM330DHCX"></a>

## 155.84 `CONFIG_ISM330DHCX`

**提示（Prompt）**：ISM330DHCX I2C/SPI 加速度计与陀螺仪芯片

**说明（Help）**

启用 ISM330DHCX 加速度计与陀螺仪传感器（Accelerometer and Gyroscope Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_ISM330DHCX_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_GPIO if n
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_ISM330DHCX
```

**定义位置（Location）**：[`drivers/sensor/st/ism330dhcx/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/ism330dhcx/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_ISM330DHCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_ISM330DHCX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_ISM330DHCX`。

<a id="CONFIG_ISM330DHCX_ENABLE_TEMP"></a>

## 155.85 `CONFIG_ISM330DHCX_ENABLE_TEMP`

**提示（Prompt）**：温度（Temperature）

**说明（Help）**

启用／禁用温度功能

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISM330DHCX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/ism330dhcx/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/ism330dhcx/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISM330DHCX I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_ISM330DHCX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ISM330DHCX_EXT_HTS221"></a>

## 155.86 `CONFIG_ISM330DHCX_EXT_HTS221`

**提示（Prompt）**：将 HTS221 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISM330DHCX_SENSORHUB && CONFIG_ISM330DHCX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/ism330dhcx/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/ism330dhcx/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISM330DHCX I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_ISM330DHCX_SENSORHUB`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX_SENSORHUB)、[`CONFIG_ISM330DHCX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ISM330DHCX_EXT_IIS2MDC"></a>

## 155.87 `CONFIG_ISM330DHCX_EXT_IIS2MDC`

**提示（Prompt）**：将 IIS2MDC 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISM330DHCX_SENSORHUB && CONFIG_ISM330DHCX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/ism330dhcx/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/ism330dhcx/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISM330DHCX I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_ISM330DHCX_SENSORHUB`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX_SENSORHUB)、[`CONFIG_ISM330DHCX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ISM330DHCX_EXT_LIS2MDL"></a>

## 155.88 `CONFIG_ISM330DHCX_EXT_LIS2MDL`

**提示（Prompt）**：将 LIS2MDL 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISM330DHCX_SENSORHUB && CONFIG_ISM330DHCX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/ism330dhcx/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/ism330dhcx/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISM330DHCX I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_ISM330DHCX_SENSORHUB`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX_SENSORHUB)、[`CONFIG_ISM330DHCX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ISM330DHCX_EXT_LPS22HB"></a>

## 155.89 `CONFIG_ISM330DHCX_EXT_LPS22HB`

**提示（Prompt）**：将 LPS22HB 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISM330DHCX_SENSORHUB && CONFIG_ISM330DHCX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/ism330dhcx/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/ism330dhcx/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISM330DHCX I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_ISM330DHCX_SENSORHUB`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX_SENSORHUB)、[`CONFIG_ISM330DHCX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ISM330DHCX_EXT_LPS22HH"></a>

## 155.90 `CONFIG_ISM330DHCX_EXT_LPS22HH`

**提示（Prompt）**：将 LPS22HH 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISM330DHCX_SENSORHUB && CONFIG_ISM330DHCX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/ism330dhcx/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/ism330dhcx/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISM330DHCX I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_ISM330DHCX_SENSORHUB`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX_SENSORHUB)、[`CONFIG_ISM330DHCX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ISM330DHCX_SENSORHUB"></a>

## 155.91 `CONFIG_ISM330DHCX_SENSORHUB`

**提示（Prompt）**：I2C 传感器集线器（Sensor Hub）功能

**说明（Help）**

启用／禁用内部传感器集线器（Sensor Hub）。最多可启用两个外部传感器；如果启用了两个以上，系统只会枚举首先找到的两个。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISM330DHCX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/ism330dhcx/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/ism330dhcx/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISM330DHCX I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_ISM330DHCX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ISM330DHCX_THREAD_PRIORITY"></a>

## 155.92 `CONFIG_ISM330DHCX_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISM330DHCX_TRIGGER_OWN_THREAD && CONFIG_ISM330DHCX_TRIGGER && CONFIG_ISM330DHCX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/ism330dhcx/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/ism330dhcx/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISM330DHCX I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_ISM330DHCX_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX_TRIGGER_OWN_THREAD)、[`CONFIG_ISM330DHCX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ISM330DHCX_TRIGGER)、[`CONFIG_ISM330DHCX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ISM330DHCX_TRIGGER`。

<a id="CONFIG_ISM330DHCX_THREAD_STACK_SIZE"></a>

## 155.93 `CONFIG_ISM330DHCX_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISM330DHCX_TRIGGER_OWN_THREAD && CONFIG_ISM330DHCX_TRIGGER && CONFIG_ISM330DHCX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/ism330dhcx/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/ism330dhcx/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISM330DHCX I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_ISM330DHCX_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX_TRIGGER_OWN_THREAD)、[`CONFIG_ISM330DHCX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ISM330DHCX_TRIGGER)、[`CONFIG_ISM330DHCX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ISM330DHCX_TRIGGER`。

<a id="CONFIG_ISM330DHCX_TRIGGER_GLOBAL_THREAD"></a>

## 155.94 `CONFIG_ISM330DHCX_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ISM330DHCX_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/ism330dhcx/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/ism330dhcx/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISM330DHCX I2C/SPI 加速度计与陀螺仪芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ISM330DHCX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ISM330DHCX_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ISM330DHCX_TRIGGER`。

<a id="CONFIG_ISM330DHCX_TRIGGER_MODE"></a>

## 155.95 `CONFIG_ISM330DHCX_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISM330DHCX && CONFIG_SENSOR
```

**可选项（Choices）**

```text
CONFIG_ISM330DHCX_TRIGGER_NONE
CONFIG_ISM330DHCX_TRIGGER_GLOBAL_THREAD
CONFIG_ISM330DHCX_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/ism330dhcx/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/ism330dhcx/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISM330DHCX I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_ISM330DHCX`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ISM330DHCX_TRIGGER_NONE`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX_TRIGGER_NONE)、[`CONFIG_ISM330DHCX_TRIGGER_GLOBAL_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX_TRIGGER_GLOBAL_THREAD)、[`CONFIG_ISM330DHCX_TRIGGER_OWN_THREAD`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX_TRIGGER_OWN_THREAD)。

<a id="CONFIG_ISM330DHCX_TRIGGER_NONE"></a>

## 155.96 `CONFIG_ISM330DHCX_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ISM330DHCX_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/ism330dhcx/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/ism330dhcx/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISM330DHCX I2C/SPI 加速度计与陀螺仪芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ISM330DHCX_TRIGGER_MODE`](P155_drivers_sensor_配置项参考_7.md#CONFIG_ISM330DHCX_TRIGGER_MODE)。

<a id="CONFIG_ISM330DHCX_TRIGGER_OWN_THREAD"></a>

## 155.97 `CONFIG_ISM330DHCX_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ISM330DHCX_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/ism330dhcx/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/ism330dhcx/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ISM330DHCX I2C/SPI 加速度计与陀螺仪芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ISM330DHCX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ISM330DHCX_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ISM330DHCX_TRIGGER`。

<a id="CONFIG_IST8310"></a>

## 155.98 `CONFIG_IST8310`

**提示（Prompt）**：IST8310 I2C 地磁芯片（Geomagnetic Chip）

**说明（Help）**

启用基于 I2C 的 IST8310 地磁传感器（Geomagnetic Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ISENTEK_IST8310_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ist8310/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ist8310/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_JC42"></a>

## 155.99 `CONFIG_JC42`

**提示（Prompt）**：JC42 温度传感器（Temperature Sensor）

**说明（Help）**

启用 JC42 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_JEDEC_JC_42_4_TEMP_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/jedec/jc42/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/jedec/jc42/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_JC42_THREAD_PRIORITY"></a>

## 155.100 `CONFIG_JC42_THREAD_PRIORITY`

**提示（Prompt）**：JC42 线程优先级（Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_JC42_TRIGGER_OWN_THREAD && CONFIG_JC42 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/jedec/jc42/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/jedec/jc42/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → JC42 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_JC42_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_JC42_TRIGGER_OWN_THREAD)、[`CONFIG_JC42`](P155_drivers_sensor_配置项参考_7.md#CONFIG_JC42)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<!-- kconfig-navigation -->

[上一章](P154_drivers_sensor_配置项参考_6.md) · [返回大纲](大纲.md) · [下一章](P156_drivers_sensor_配置项参考_8.md)
