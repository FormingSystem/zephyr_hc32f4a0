---
id: learning.zephyr-docs.kconfig-reference.page-156
title: "`drivers/sensor`配置项参考（8/15）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第156章\_`drivers/sensor`配置项参考（8/15）

本章翻译官方 Kconfig 数据库中 `drivers/sensor` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_JC42_THREAD_STACK_SIZE"></a>

## 156.1 `CONFIG_JC42_THREAD_STACK_SIZE`

**提示（Prompt）**：传感器延迟工作（Delayed Work）线程栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_JC42_TRIGGER_OWN_THREAD && CONFIG_JC42 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/jedec/jc42/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/jedec/jc42/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → JC42 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_JC42_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_JC42_TRIGGER_OWN_THREAD)、[`CONFIG_JC42`](P155_drivers_sensor_配置项参考_7.md#CONFIG_JC42)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_JC42_TRIGGER_GLOBAL_THREAD"></a>

## 156.2 `CONFIG_JC42_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_JC42_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/jedec/jc42/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/jedec/jc42/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → JC42 温度传感器（Temperature Sensor） → JC42 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_JC42_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JC42_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_JC42_TRIGGER`。

<a id="CONFIG_JC42_TRIGGER_NONE"></a>

## 156.3 `CONFIG_JC42_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/jedec/jc42/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/jedec/jc42/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → JC42 温度传感器（Temperature Sensor） → JC42 触发模式（Trigger Mode）

<a id="CONFIG_JC42_TRIGGER_OWN_THREAD"></a>

## 156.4 `CONFIG_JC42_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_JC42_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/jedec/jc42/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/jedec/jc42/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → JC42 温度传感器（Temperature Sensor） → JC42 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_JC42_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JC42_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_JC42_TRIGGER`。

<a id="CONFIG_LIS2DE12"></a>

## 156.5 `CONFIG_LIS2DE12`

**提示（Prompt）**：LIS2DE12 I2C/SPI smartxl 芯片

**说明（Help）**

启用 LIS2DE12 smartxl 传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LIS2DE12_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
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
CONFIG_USE_STDC_LIS2DE12
```

**定义位置（Location）**：[`drivers/sensor/st/lis2de12/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2de12/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_LIS2DE12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LIS2DE12)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_LIS2DE12`。

<a id="CONFIG_LIS2DE12_ENABLE_TEMP"></a>

## 156.6 `CONFIG_LIS2DE12_ENABLE_TEMP`

**提示（Prompt）**：芯片裸片温度传感器（Die Temperature Sensor）

**说明（Help）**

启用／禁用芯片裸片温度传感器（Die Temperature Sensor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DE12 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lis2de12/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2de12/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DE12 I2C/SPI smartxl 芯片

**配置项引用（Symbol References）**：[`CONFIG_LIS2DE12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DE12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS2DE12_THREAD_PRIORITY"></a>

## 156.7 `CONFIG_LIS2DE12_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DE12_TRIGGER_OWN_THREAD && CONFIG_LIS2DE12_TRIGGER && CONFIG_LIS2DE12 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DE12 I2C/SPI smartxl 芯片

**配置项引用（Symbol References）**：[`CONFIG_LIS2DE12_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DE12_TRIGGER_OWN_THREAD)、[`CONFIG_LIS2DE12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DE12_TRIGGER)、[`CONFIG_LIS2DE12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DE12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DE12_TRIGGER`。

<a id="CONFIG_LIS2DE12_THREAD_STACK_SIZE"></a>

## 156.8 `CONFIG_LIS2DE12_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DE12_TRIGGER_OWN_THREAD && CONFIG_LIS2DE12_TRIGGER && CONFIG_LIS2DE12 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DE12 I2C/SPI smartxl 芯片

**配置项引用（Symbol References）**：[`CONFIG_LIS2DE12_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DE12_TRIGGER_OWN_THREAD)、[`CONFIG_LIS2DE12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DE12_TRIGGER)、[`CONFIG_LIS2DE12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DE12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DE12_TRIGGER`。

<a id="CONFIG_LIS2DE12_TRIGGER_GLOBAL_THREAD"></a>

## 156.9 `CONFIG_LIS2DE12_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_LIS2DE12_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_LIS2DE12_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DE12 I2C/SPI smartxl 芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_LIS2DE12_TRIGGER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DE12_TRIGGER_MODE)、[`CONFIG_LIS2DE12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DE12_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DE12_TRIGGER`。

<a id="CONFIG_LIS2DE12_TRIGGER_MODE"></a>

## 156.10 `CONFIG_LIS2DE12_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定传感器模块使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DE12 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_LIS2DE12_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_LIS2DE12_TRIGGER_NONE
CONFIG_LIS2DE12_TRIGGER_GLOBAL_THREAD
CONFIG_LIS2DE12_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DE12 I2C/SPI smartxl 芯片

**配置项引用（Symbol References）**：[`CONFIG_LIS2DE12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DE12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LIS2DE12_TRIGGER_NONE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DE12_TRIGGER_NONE)、[`CONFIG_LIS2DE12_TRIGGER_GLOBAL_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DE12_TRIGGER_GLOBAL_THREAD)、[`CONFIG_LIS2DE12_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DE12_TRIGGER_OWN_THREAD)。

<a id="CONFIG_LIS2DE12_TRIGGER_NONE"></a>

## 156.11 `CONFIG_LIS2DE12_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DE12_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DE12 I2C/SPI smartxl 芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DE12_TRIGGER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DE12_TRIGGER_MODE)。

<a id="CONFIG_LIS2DE12_TRIGGER_OWN_THREAD"></a>

## 156.12 `CONFIG_LIS2DE12_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_LIS2DE12_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_LIS2DE12_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DE12 I2C/SPI smartxl 芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_LIS2DE12_TRIGGER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DE12_TRIGGER_MODE)、[`CONFIG_LIS2DE12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DE12_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DE12_TRIGGER`。

<a id="CONFIG_LIS2DH"></a>

## 156.13 `CONFIG_LIS2DH`

**提示（Prompt）**：LIS2DH 三轴加速度计（Three Axis Accelerometer）

**说明（Help）**

启用基于 SPI/I2C 的 LIS2DH、LIS3DH、LSM303DLHC、LIS2DH12 和 LSM303AGR 三轴加速度传感器（Triaxial Accelerometer Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LIS2DH_ENABLED && CONFIG_SENSOR
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
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_LIS2DH_ACCEL_HP_FILTERS"></a>

## 156.14 `CONFIG_LIS2DH_ACCEL_HP_FILTERS`

**提示（Prompt）**：为中断线上的 AOI 功能设置高通滤波器（High Pass Filter）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DH && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L147)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS2DH_ACCEL_RANGE"></a>

## 156.15 `CONFIG_LIS2DH_ACCEL_RANGE`

**提示（Prompt）**：加速度测量量程（Measurement Range）

**说明（Help）**

加速度值的初始测量满量程范围（Full Scale Range）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DH && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_LIS2DH_ACCEL_RANGE_RUNTIME
```

**可选项（Choices）**

```text
CONFIG_LIS2DH_ACCEL_RANGE_RUNTIME
CONFIG_LIS2DH_ACCEL_RANGE_2G
CONFIG_LIS2DH_ACCEL_RANGE_4G
CONFIG_LIS2DH_ACCEL_RANGE_8G
CONFIG_LIS2DH_ACCEL_RANGE_16G
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LIS2DH_ACCEL_RANGE_RUNTIME`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ACCEL_RANGE_RUNTIME)、[`CONFIG_LIS2DH_ACCEL_RANGE_2G`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ACCEL_RANGE_2G)、[`CONFIG_LIS2DH_ACCEL_RANGE_4G`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ACCEL_RANGE_4G)、[`CONFIG_LIS2DH_ACCEL_RANGE_8G`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ACCEL_RANGE_8G)、[`CONFIG_LIS2DH_ACCEL_RANGE_16G`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ACCEL_RANGE_16G)。

<a id="CONFIG_LIS2DH_ACCEL_RANGE_16G"></a>

## 156.16 `CONFIG_LIS2DH_ACCEL_RANGE_16G`

**提示（Prompt）**：±16 g

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_ACCEL_RANGE>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 加速度测量量程（Measurement Range）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_ACCEL_RANGE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ACCEL_RANGE)。

<a id="CONFIG_LIS2DH_ACCEL_RANGE_2G"></a>

## 156.17 `CONFIG_LIS2DH_ACCEL_RANGE_2G`

**提示（Prompt）**：±2 g

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_ACCEL_RANGE>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 加速度测量量程（Measurement Range）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_ACCEL_RANGE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ACCEL_RANGE)。

<a id="CONFIG_LIS2DH_ACCEL_RANGE_4G"></a>

## 156.18 `CONFIG_LIS2DH_ACCEL_RANGE_4G`

**提示（Prompt）**：±4 g

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_ACCEL_RANGE>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 加速度测量量程（Measurement Range）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_ACCEL_RANGE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ACCEL_RANGE)。

<a id="CONFIG_LIS2DH_ACCEL_RANGE_8G"></a>

## 156.19 `CONFIG_LIS2DH_ACCEL_RANGE_8G`

**提示（Prompt）**：±8 g

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_ACCEL_RANGE>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 加速度测量量程（Measurement Range）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_ACCEL_RANGE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ACCEL_RANGE)。

<a id="CONFIG_LIS2DH_ACCEL_RANGE_RUNTIME"></a>

## 156.20 `CONFIG_LIS2DH_ACCEL_RANGE_RUNTIME`

**提示（Prompt）**：在运行时设置（Set at Runtime）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_ACCEL_RANGE>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 加速度测量量程（Measurement Range）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_ACCEL_RANGE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ACCEL_RANGE)。

<a id="CONFIG_LIS2DH_BLOCK_DATA_UPDATE"></a>

## 156.21 `CONFIG_LIS2DH_BLOCK_DATA_UPDATE`

**提示（Prompt）**：在最高有效字节（MSB）和最低有效字节（LSB）均被读取之前，不更新输出寄存器

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DH && CONFIG_SENSOR
```

**被选择（Selected by）**

```text
CONFIG_LIS2DH_MEASURE_TEMPERATURE
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LIS2DH_MEASURE_TEMPERATURE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_MEASURE_TEMPERATURE)。

<a id="CONFIG_LIS2DH_MEASURE_TEMPERATURE"></a>

## 156.22 `CONFIG_LIS2DH_MEASURE_TEMPERATURE`

**提示（Prompt）**：温度测量（Temperature Measurements）

**说明（Help）**

该温度传感器最适合测量相对温度，例如变冷或变暖了 X 摄氏度。每颗芯片都有偏移量（Offset），必须将该偏移量应用于测量结果。可通过将报告温度与参考温度比较来确定偏移量。原文注明，此选项不适用于 LSM330DLHC。

译注：本条原文型号为 LSM330DLHC；驱动总说明列出的型号为 LSM303DLHC，此处保留两处原文差异。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DH && CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_LIS2DH_BLOCK_DATA_UPDATE
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LIS2DH_BLOCK_DATA_UPDATE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_BLOCK_DATA_UPDATE)。

<a id="CONFIG_LIS2DH_ODR"></a>

## 156.23 `CONFIG_LIS2DH_ODR`

**提示（Prompt）**：输出数据速率频率（Output Data Rate Frequency）

**说明（Help）**

初始化时设置的加速度数据初始输出频率。支持的值为：

- 所有功耗模式：1 Hz、10 Hz、25 Hz、50 Hz、100 Hz、200 Hz、400 Hz。
- 仅低功耗模式（Low Power Mode）：1620 Hz、5376 Hz。
- 正常功耗模式（Normal Power Mode）：1344 Hz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DH && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_LIS2DH_ODR_RUNTIME
```

**可选项（Choices）**

```text
CONFIG_LIS2DH_ODR_RUNTIME
CONFIG_LIS2DH_ODR_1
CONFIG_LIS2DH_ODR_2
CONFIG_LIS2DH_ODR_3
CONFIG_LIS2DH_ODR_4
CONFIG_LIS2DH_ODR_5
CONFIG_LIS2DH_ODR_6
CONFIG_LIS2DH_ODR_7
CONFIG_LIS2DH_ODR_8
CONFIG_LIS2DH_ODR_9_NORMAL
CONFIG_LIS2DH_ODR_9_LOW
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LIS2DH_ODR_RUNTIME`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR_RUNTIME)、[`CONFIG_LIS2DH_ODR_1`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR_1)、[`CONFIG_LIS2DH_ODR_2`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR_2)、[`CONFIG_LIS2DH_ODR_3`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR_3)、[`CONFIG_LIS2DH_ODR_4`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR_4)、[`CONFIG_LIS2DH_ODR_5`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR_5)、[`CONFIG_LIS2DH_ODR_6`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR_6)、[`CONFIG_LIS2DH_ODR_7`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR_7)、[`CONFIG_LIS2DH_ODR_8`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR_8)、[`CONFIG_LIS2DH_ODR_9_NORMAL`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR_9_NORMAL)、[`CONFIG_LIS2DH_ODR_9_LOW`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR_9_LOW)。

<a id="CONFIG_LIS2DH_ODR_1"></a>

## 156.24 `CONFIG_LIS2DH_ODR_1`

**提示（Prompt）**：1 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_ODR>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 输出数据速率频率（Output Data Rate Frequency）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_ODR`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR)。

<a id="CONFIG_LIS2DH_ODR_2"></a>

## 156.25 `CONFIG_LIS2DH_ODR_2`

**提示（Prompt）**：10 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_ODR>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 输出数据速率频率（Output Data Rate Frequency）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_ODR`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR)。

<a id="CONFIG_LIS2DH_ODR_3"></a>

## 156.26 `CONFIG_LIS2DH_ODR_3`

**提示（Prompt）**：25 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_ODR>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 输出数据速率频率（Output Data Rate Frequency）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_ODR`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR)。

<a id="CONFIG_LIS2DH_ODR_4"></a>

## 156.27 `CONFIG_LIS2DH_ODR_4`

**提示（Prompt）**：50 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_ODR>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 输出数据速率频率（Output Data Rate Frequency）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_ODR`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR)。

<a id="CONFIG_LIS2DH_ODR_5"></a>

## 156.28 `CONFIG_LIS2DH_ODR_5`

**提示（Prompt）**：100 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_ODR>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 输出数据速率频率（Output Data Rate Frequency）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_ODR`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR)。

<a id="CONFIG_LIS2DH_ODR_6"></a>

## 156.29 `CONFIG_LIS2DH_ODR_6`

**提示（Prompt）**：200 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_ODR>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 输出数据速率频率（Output Data Rate Frequency）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_ODR`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR)。

<a id="CONFIG_LIS2DH_ODR_7"></a>

## 156.30 `CONFIG_LIS2DH_ODR_7`

**提示（Prompt）**：400 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_ODR>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 输出数据速率频率（Output Data Rate Frequency）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_ODR`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR)。

<a id="CONFIG_LIS2DH_ODR_8"></a>

## 156.31 `CONFIG_LIS2DH_ODR_8`

**提示（Prompt）**：1.6 kHz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DH_OPER_MODE_LOW_POWER && <choice CONFIG_LIS2DH_ODR>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 输出数据速率频率（Output Data Rate Frequency）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_OPER_MODE_LOW_POWER`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_OPER_MODE_LOW_POWER)、[`CONFIG_LIS2DH_ODR`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR)。

<a id="CONFIG_LIS2DH_ODR_9_LOW"></a>

## 156.32 `CONFIG_LIS2DH_ODR_9_LOW`

**提示（Prompt）**：5 kHz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DH_OPER_MODE_LOW_POWER && <choice CONFIG_LIS2DH_ODR>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 输出数据速率频率（Output Data Rate Frequency）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_OPER_MODE_LOW_POWER`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_OPER_MODE_LOW_POWER)、[`CONFIG_LIS2DH_ODR`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR)。

<a id="CONFIG_LIS2DH_ODR_9_NORMAL"></a>

## 156.33 `CONFIG_LIS2DH_ODR_9_NORMAL`

**提示（Prompt）**：1.25 kHz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_LIS2DH_OPER_MODE_NORMAL || CONFIG_LIS2DH_OPER_MODE_HIGH_RES) && <choice CONFIG_LIS2DH_ODR>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 输出数据速率频率（Output Data Rate Frequency）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_OPER_MODE_NORMAL`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_OPER_MODE_NORMAL)、[`CONFIG_LIS2DH_OPER_MODE_HIGH_RES`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_OPER_MODE_HIGH_RES)、[`CONFIG_LIS2DH_ODR`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR)。

<a id="CONFIG_LIS2DH_ODR_RUNTIME"></a>

## 156.34 `CONFIG_LIS2DH_ODR_RUNTIME`

**提示（Prompt）**：在运行时设置（Set at Runtime）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_ODR>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 输出数据速率频率（Output Data Rate Frequency）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_ODR`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_ODR)。

<a id="CONFIG_LIS2DH_OPER_MODE"></a>

## 156.35 `CONFIG_LIS2DH_OPER_MODE`

**提示（Prompt）**：工作模式（Operation Mode）

**说明（Help）**

选择芯片初始化时使用高分辨率（High Resolution）、正常（Normal）或低功耗（Low Power）工作模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DH && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_LIS2DH_OPER_MODE_NORMAL
```

**可选项（Choices）**

```text
CONFIG_LIS2DH_OPER_MODE_HIGH_RES
CONFIG_LIS2DH_OPER_MODE_NORMAL
CONFIG_LIS2DH_OPER_MODE_LOW_POWER
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LIS2DH_OPER_MODE_NORMAL`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_OPER_MODE_NORMAL)、[`CONFIG_LIS2DH_OPER_MODE_HIGH_RES`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_OPER_MODE_HIGH_RES)、[`CONFIG_LIS2DH_OPER_MODE_LOW_POWER`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_OPER_MODE_LOW_POWER)。

<a id="CONFIG_LIS2DH_OPER_MODE_HIGH_RES"></a>

## 156.36 `CONFIG_LIS2DH_OPER_MODE_HIGH_RES`

**提示（Prompt）**：高分辨率（High Resolution，12 位）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_OPER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 工作模式（Operation Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_OPER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_OPER_MODE)。

<a id="CONFIG_LIS2DH_OPER_MODE_LOW_POWER"></a>

## 156.37 `CONFIG_LIS2DH_OPER_MODE_LOW_POWER`

**提示（Prompt）**：低功耗（Low Power，8 位）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_OPER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 工作模式（Operation Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_OPER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_OPER_MODE)。

<a id="CONFIG_LIS2DH_OPER_MODE_NORMAL"></a>

## 156.38 `CONFIG_LIS2DH_OPER_MODE_NORMAL`

**提示（Prompt）**：正常（Normal，10 位）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_OPER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 工作模式（Operation Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_OPER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_OPER_MODE)。

<a id="CONFIG_LIS2DH_SELF_TEST"></a>

## 156.39 `CONFIG_LIS2DH_SELF_TEST`

**提示（Prompt）**：自检属性（Self Test Attribute）

**说明（Help）**

启用对传感器自检位（Self Test Bits）的配置支持。适用的自检流程请参阅传感器数据手册。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DH && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:165`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L165)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS2DH_THREAD_PRIORITY"></a>

## 156.40 `CONFIG_LIS2DH_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DH_TRIGGER_OWN_THREAD && CONFIG_LIS2DH && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_TRIGGER_OWN_THREAD)、[`CONFIG_LIS2DH`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS2DH_THREAD_STACK_SIZE"></a>

## 156.41 `CONFIG_LIS2DH_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DH_TRIGGER_OWN_THREAD && CONFIG_LIS2DH && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_TRIGGER_OWN_THREAD)、[`CONFIG_LIS2DH`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS2DH_TRIGGER_GLOBAL_THREAD"></a>

## 156.42 `CONFIG_LIS2DH_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LIS2DH_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DH_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DH_TRIGGER`。

<a id="CONFIG_LIS2DH_TRIGGER_MODE"></a>

## 156.43 `CONFIG_LIS2DH_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DH && CONFIG_SENSOR
```

**可选项（Choices）**

```text
CONFIG_LIS2DH_TRIGGER_NONE
CONFIG_LIS2DH_TRIGGER_GLOBAL_THREAD
CONFIG_LIS2DH_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LIS2DH_TRIGGER_NONE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_TRIGGER_NONE)、[`CONFIG_LIS2DH_TRIGGER_GLOBAL_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_TRIGGER_GLOBAL_THREAD)、[`CONFIG_LIS2DH_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_TRIGGER_OWN_THREAD)。

<a id="CONFIG_LIS2DH_TRIGGER_NONE"></a>

## 156.44 `CONFIG_LIS2DH_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DH_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_TRIGGER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DH_TRIGGER_MODE)。

<a id="CONFIG_LIS2DH_TRIGGER_OWN_THREAD"></a>

## 156.45 `CONFIG_LIS2DH_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LIS2DH_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dh/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dh/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DH 三轴加速度计（Three Axis Accelerometer） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DH_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DH_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DH_TRIGGER`。

<a id="CONFIG_LIS2DS12"></a>

## 156.46 `CONFIG_LIS2DS12`

**提示（Prompt）**：LIS2DS12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**说明（Help）**

启用 LIS2DS12 加速度传感器（Accelerometer Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LIS2DS12_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
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
CONFIG_USE_STDC_LIS2DS12
```

**定义位置（Location）**：[`drivers/sensor/st/lis2ds12/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2ds12/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_LIS2DS12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LIS2DS12)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_LIS2DS12`。

<a id="CONFIG_LIS2DS12_ENABLE_TEMP"></a>

## 156.47 `CONFIG_LIS2DS12_ENABLE_TEMP`

**提示（Prompt）**：温度（Temperature）

**说明（Help）**

启用／禁用温度功能

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DS12 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lis2ds12/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2ds12/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DS12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIS2DS12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DS12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS2DS12_THREAD_PRIORITY"></a>

## 156.48 `CONFIG_LIS2DS12_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DS12_TRIGGER_OWN_THREAD && CONFIG_LIS2DS12 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/lis2ds12/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2ds12/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DS12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIS2DS12_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DS12_TRIGGER_OWN_THREAD)、[`CONFIG_LIS2DS12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DS12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS2DS12_THREAD_STACK_SIZE"></a>

## 156.49 `CONFIG_LIS2DS12_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DS12_TRIGGER_OWN_THREAD && CONFIG_LIS2DS12 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/lis2ds12/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2ds12/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DS12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIS2DS12_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DS12_TRIGGER_OWN_THREAD)、[`CONFIG_LIS2DS12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DS12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS2DS12_TRIGGER_GLOBAL_THREAD"></a>

## 156.50 `CONFIG_LIS2DS12_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LIS2DS12_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lis2ds12/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2ds12/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DS12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DS12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DS12_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DS12_TRIGGER`。

<a id="CONFIG_LIS2DS12_TRIGGER_MODE"></a>

## 156.51 `CONFIG_LIS2DS12_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DS12 && CONFIG_SENSOR
```

**可选项（Choices）**

```text
CONFIG_LIS2DS12_TRIGGER_NONE
CONFIG_LIS2DS12_TRIGGER_GLOBAL_THREAD
CONFIG_LIS2DS12_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/lis2ds12/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2ds12/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DS12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIS2DS12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DS12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LIS2DS12_TRIGGER_NONE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DS12_TRIGGER_NONE)、[`CONFIG_LIS2DS12_TRIGGER_GLOBAL_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DS12_TRIGGER_GLOBAL_THREAD)、[`CONFIG_LIS2DS12_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DS12_TRIGGER_OWN_THREAD)。

<a id="CONFIG_LIS2DS12_TRIGGER_NONE"></a>

## 156.52 `CONFIG_LIS2DS12_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DS12_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2ds12/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2ds12/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DS12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DS12_TRIGGER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DS12_TRIGGER_MODE)。

<a id="CONFIG_LIS2DS12_TRIGGER_OWN_THREAD"></a>

## 156.53 `CONFIG_LIS2DS12_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LIS2DS12_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lis2ds12/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2ds12/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DS12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DS12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DS12_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DS12_TRIGGER`。

<a id="CONFIG_LIS2DU12"></a>

## 156.54 `CONFIG_LIS2DU12`

**提示（Prompt）**：LIS2DU12 I2C/SPI smartxl 芯片

**说明（Help）**

启用 LIS2DU12 smartxl 传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LIS2DU12_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
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
CONFIG_USE_STDC_LIS2DU12
```

**定义位置（Location）**：[`drivers/sensor/st/lis2du12/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2du12/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_LIS2DU12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LIS2DU12)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_LIS2DU12`。

<a id="CONFIG_LIS2DU12_THREAD_PRIORITY"></a>

## 156.55 `CONFIG_LIS2DU12_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DU12_TRIGGER_OWN_THREAD && CONFIG_LIS2DU12_TRIGGER && CONFIG_LIS2DU12 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DU12 I2C/SPI smartxl 芯片

**配置项引用（Symbol References）**：[`CONFIG_LIS2DU12_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DU12_TRIGGER_OWN_THREAD)、[`CONFIG_LIS2DU12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DU12_TRIGGER)、[`CONFIG_LIS2DU12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DU12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DU12_TRIGGER`。

<a id="CONFIG_LIS2DU12_THREAD_STACK_SIZE"></a>

## 156.56 `CONFIG_LIS2DU12_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DU12_TRIGGER_OWN_THREAD && CONFIG_LIS2DU12_TRIGGER && CONFIG_LIS2DU12 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DU12 I2C/SPI smartxl 芯片

**配置项引用（Symbol References）**：[`CONFIG_LIS2DU12_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DU12_TRIGGER_OWN_THREAD)、[`CONFIG_LIS2DU12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DU12_TRIGGER)、[`CONFIG_LIS2DU12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DU12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DU12_TRIGGER`。

<a id="CONFIG_LIS2DU12_TRIGGER_GLOBAL_THREAD"></a>

## 156.57 `CONFIG_LIS2DU12_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_LIS2DU12_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_LIS2DU12_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DU12 I2C/SPI smartxl 芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_LIS2DU12_TRIGGER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DU12_TRIGGER_MODE)、[`CONFIG_LIS2DU12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DU12_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DU12_TRIGGER`。

<a id="CONFIG_LIS2DU12_TRIGGER_MODE"></a>

## 156.58 `CONFIG_LIS2DU12_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定传感器模块使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DU12 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_LIS2DU12_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_LIS2DU12_TRIGGER_NONE
CONFIG_LIS2DU12_TRIGGER_GLOBAL_THREAD
CONFIG_LIS2DU12_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DU12 I2C/SPI smartxl 芯片

**配置项引用（Symbol References）**：[`CONFIG_LIS2DU12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DU12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LIS2DU12_TRIGGER_NONE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DU12_TRIGGER_NONE)、[`CONFIG_LIS2DU12_TRIGGER_GLOBAL_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DU12_TRIGGER_GLOBAL_THREAD)、[`CONFIG_LIS2DU12_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DU12_TRIGGER_OWN_THREAD)。

<a id="CONFIG_LIS2DU12_TRIGGER_NONE"></a>

## 156.59 `CONFIG_LIS2DU12_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DU12_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DU12 I2C/SPI smartxl 芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DU12_TRIGGER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DU12_TRIGGER_MODE)。

<a id="CONFIG_LIS2DU12_TRIGGER_OWN_THREAD"></a>

## 156.60 `CONFIG_LIS2DU12_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_LIS2DU12_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_LIS2DU12_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DU12 I2C/SPI smartxl 芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_LIS2DU12_TRIGGER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DU12_TRIGGER_MODE)、[`CONFIG_LIS2DU12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DU12_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DU12_TRIGGER`。

<a id="CONFIG_LIS2DUX12"></a>

## 156.61 `CONFIG_LIS2DUX12`

**提示（Prompt）**：LIS2DUX12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**说明（Help）**

启用 LIS2DUX12 加速度传感器（Accelerometer Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_LIS2DUX12_ENABLED || DT_HAS_ST_LIS2DUXS12_ENABLED) && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n || n
CONFIG_SPI if n || n
CONFIG_GPIO if n || n || n || n
CONFIG_I2C_RTIO if CONFIG_I2C && CONFIG_SENSOR_ASYNC_API
CONFIG_SPI_RTIO if CONFIG_SPI && CONFIG_SENSOR_ASYNC_API
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_LIS2DUX12 if DT_HAS_ST_LIS2DUX12_ENABLED
CONFIG_USE_STDC_LIS2DUXS12 if DT_HAS_ST_LIS2DUXS12_ENABLED
CONFIG_RTIO_WORKQ if CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dux12/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dux12/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_LIS2DUX12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LIS2DUX12)、[`CONFIG_USE_STDC_LIS2DUXS12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LIS2DUXS12)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_LIS2DUX12`、`CONFIG_USE_STDC_LIS2DUXS12`。

<a id="CONFIG_LIS2DUX12_ENABLE_TEMP"></a>

## 156.62 `CONFIG_LIS2DUX12_ENABLE_TEMP`

**提示（Prompt）**：温度（Temperature）

**说明（Help）**

启用／禁用温度功能

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DUX12 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dux12/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dux12/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DUX12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIS2DUX12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS2DUX12_STREAM"></a>

## 156.63 `CONFIG_LIS2DUX12_STREAM`

**提示（Prompt）**：使用硬件先入先出队列（FIFO）流式传输数据

**说明（Help）**

使用此配置选项，启用通过实时 I/O（RTIO）子系统流式传输传感器数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_I2C_RTIO || CONFIG_SPI_RTIO) && CONFIG_SENSOR_ASYNC_API && CONFIG_LIS2DUX12 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_LIS2DUX12_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dux12/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dux12/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DUX12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_LIS2DUX12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LIS2DUX12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DUX12_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DUX12_TRIGGER`。

<a id="CONFIG_LIS2DUX12_THREAD_PRIORITY"></a>

## 156.64 `CONFIG_LIS2DUX12_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DUX12_TRIGGER_OWN_THREAD && CONFIG_LIS2DUX12_TRIGGER && CONFIG_LIS2DUX12 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DUX12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIS2DUX12_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12_TRIGGER_OWN_THREAD)、[`CONFIG_LIS2DUX12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DUX12_TRIGGER)、[`CONFIG_LIS2DUX12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DUX12_TRIGGER`。

<a id="CONFIG_LIS2DUX12_THREAD_STACK_SIZE"></a>

## 156.65 `CONFIG_LIS2DUX12_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DUX12_TRIGGER_OWN_THREAD && CONFIG_LIS2DUX12_TRIGGER && CONFIG_LIS2DUX12 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DUX12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIS2DUX12_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12_TRIGGER_OWN_THREAD)、[`CONFIG_LIS2DUX12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DUX12_TRIGGER)、[`CONFIG_LIS2DUX12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DUX12_TRIGGER`。

<a id="CONFIG_LIS2DUX12_TRIGGER_GLOBAL_THREAD"></a>

## 156.66 `CONFIG_LIS2DUX12_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_LIS2DUX12_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_LIS2DUX12_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DUX12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_LIS2DUX12_TRIGGER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12_TRIGGER_MODE)、[`CONFIG_LIS2DUX12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DUX12_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DUX12_TRIGGER`。

<a id="CONFIG_LIS2DUX12_TRIGGER_MODE"></a>

## 156.67 `CONFIG_LIS2DUX12_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定传感器模块使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DUX12 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_LIS2DUX12_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_LIS2DUX12_TRIGGER_NONE
CONFIG_LIS2DUX12_TRIGGER_GLOBAL_THREAD
CONFIG_LIS2DUX12_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DUX12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIS2DUX12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LIS2DUX12_TRIGGER_NONE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12_TRIGGER_NONE)、[`CONFIG_LIS2DUX12_TRIGGER_GLOBAL_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12_TRIGGER_GLOBAL_THREAD)、[`CONFIG_LIS2DUX12_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12_TRIGGER_OWN_THREAD)。

<a id="CONFIG_LIS2DUX12_TRIGGER_NONE"></a>

## 156.68 `CONFIG_LIS2DUX12_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DUX12_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DUX12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DUX12_TRIGGER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12_TRIGGER_MODE)。

<a id="CONFIG_LIS2DUX12_TRIGGER_OWN_THREAD"></a>

## 156.69 `CONFIG_LIS2DUX12_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_LIS2DUX12_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_LIS2DUX12_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DUX12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_LIS2DUX12_TRIGGER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12_TRIGGER_MODE)、[`CONFIG_LIS2DUX12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DUX12_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DUX12_TRIGGER`。

<a id="CONFIG_LIS2DW12"></a>

## 156.70 `CONFIG_LIS2DW12`

**提示（Prompt）**：LIS2DW12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**说明（Help）**

启用 LIS2DW12 加速度传感器（Accelerometer Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LIS2DW12_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
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
CONFIG_USE_STDC_LIS2DW12
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dw12/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dw12/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_LIS2DW12`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LIS2DW12)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_LIS2DW12`。

<a id="CONFIG_LIS2DW12_FREEFALL"></a>

## 156.71 `CONFIG_LIS2DW12_FREEFALL`

**提示（Prompt）**：自由落体检测（Free Fall Detection，通过中断）

**说明（Help）**

通过中断启用自由落体检测（Freefall Detection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DW12 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dw12/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dw12/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DW12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIS2DW12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DW12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS2DW12_SLEEP"></a>

## 156.72 `CONFIG_LIS2DW12_SLEEP`

**提示（Prompt）**：睡眠模式（Sleep Mode）

**说明（Help）**

启用睡眠（非活动，Inactivity）模式，在检测到非活动时改变输出数据速率（ODR）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DW12 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dw12/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dw12/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DW12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIS2DW12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DW12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS2DW12_TAP"></a>

## 156.73 `CONFIG_LIS2DW12_TAP`

**提示（Prompt）**：单击与双击检测（Tap and Tap-Tap Detection）

**说明（Help）**

启用敲击检测（Tap Detection），包括单击和双击。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DW12_TRIGGER && CONFIG_LIS2DW12 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dw12/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dw12/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DW12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIS2DW12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DW12_TRIGGER)、[`CONFIG_LIS2DW12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DW12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DW12_TRIGGER`。

<a id="CONFIG_LIS2DW12_THREAD_PRIORITY"></a>

## 156.74 `CONFIG_LIS2DW12_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DW12_TRIGGER_OWN_THREAD && CONFIG_LIS2DW12_TRIGGER && CONFIG_LIS2DW12 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dw12/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dw12/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DW12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIS2DW12_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DW12_TRIGGER_OWN_THREAD)、[`CONFIG_LIS2DW12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DW12_TRIGGER)、[`CONFIG_LIS2DW12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DW12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DW12_TRIGGER`。

<a id="CONFIG_LIS2DW12_THREAD_STACK_SIZE"></a>

## 156.75 `CONFIG_LIS2DW12_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DW12_TRIGGER_OWN_THREAD && CONFIG_LIS2DW12_TRIGGER && CONFIG_LIS2DW12 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dw12/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dw12/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DW12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIS2DW12_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DW12_TRIGGER_OWN_THREAD)、[`CONFIG_LIS2DW12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DW12_TRIGGER)、[`CONFIG_LIS2DW12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DW12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DW12_TRIGGER`。

<a id="CONFIG_LIS2DW12_TRIGGER_GLOBAL_THREAD"></a>

## 156.76 `CONFIG_LIS2DW12_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LIS2DW12_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dw12/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dw12/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DW12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DW12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DW12_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DW12_TRIGGER`。

<a id="CONFIG_LIS2DW12_TRIGGER_MODE"></a>

## 156.77 `CONFIG_LIS2DW12_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DW12 && CONFIG_SENSOR
```

**可选项（Choices）**

```text
CONFIG_LIS2DW12_TRIGGER_NONE
CONFIG_LIS2DW12_TRIGGER_GLOBAL_THREAD
CONFIG_LIS2DW12_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dw12/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dw12/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DW12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIS2DW12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DW12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LIS2DW12_TRIGGER_NONE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DW12_TRIGGER_NONE)、[`CONFIG_LIS2DW12_TRIGGER_GLOBAL_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DW12_TRIGGER_GLOBAL_THREAD)、[`CONFIG_LIS2DW12_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DW12_TRIGGER_OWN_THREAD)。

<a id="CONFIG_LIS2DW12_TRIGGER_NONE"></a>

## 156.78 `CONFIG_LIS2DW12_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2DW12_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dw12/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dw12/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DW12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DW12_TRIGGER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DW12_TRIGGER_MODE)。

<a id="CONFIG_LIS2DW12_TRIGGER_OWN_THREAD"></a>

## 156.79 `CONFIG_LIS2DW12_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LIS2DW12_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dw12/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dw12/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DW12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2DW12_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2DW12_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2DW12_TRIGGER`。

<a id="CONFIG_LIS2DW12_WAKEUP"></a>

## 156.80 `CONFIG_LIS2DW12_WAKEUP`

**提示（Prompt）**：唤醒检测（Wakeup Detection，通过中断）

**说明（Help）**

启用唤醒检测（Wakeup Detection）功能。如果一定数量的连续数据超过所配置的阈值，就会产生唤醒中断信号；阈值通过设备树（DT）配置。阈值同时适用于正值和负值数据：三个轴中至少有一个轴的幅值超过阈值，才会产生唤醒中断。有关此功能的更多信息，请参阅 ST AN5038。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2DW12 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lis2dw12/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2dw12/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2DW12 I2C/SPI 加速度传感器（Accelerometer Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIS2DW12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DW12)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS2MDL"></a>

## 156.81 `CONFIG_LIS2MDL`

**提示（Prompt）**：LIS2MDL 磁力计（Magnetometer）

**说明（Help）**

启用基于 I2C 的 LIS2MDL 磁力计传感器（Magnetometer Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LIS2MDL_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
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
CONFIG_USE_STDC_LIS2MDL
```

**定义位置（Location）**：[`drivers/sensor/st/lis2mdl/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2mdl/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_LIS2MDL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LIS2MDL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_LIS2MDL`。

<a id="CONFIG_LIS2MDL_MAG_ODR_RUNTIME"></a>

## 156.82 `CONFIG_LIS2MDL_MAG_ODR_RUNTIME`

**提示（Prompt）**：在运行时设置磁力计采样频率（ODR），默认值为 10 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2MDL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lis2mdl/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2mdl/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2MDL 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS2MDL`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2MDL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS2MDL_THREAD_PRIORITY"></a>

## 156.83 `CONFIG_LIS2MDL_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2MDL_TRIGGER_OWN_THREAD && CONFIG_LIS2MDL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/lis2mdl/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2mdl/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2MDL 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS2MDL_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2MDL_TRIGGER_OWN_THREAD)、[`CONFIG_LIS2MDL`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2MDL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS2MDL_THREAD_STACK_SIZE"></a>

## 156.84 `CONFIG_LIS2MDL_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2MDL_TRIGGER_OWN_THREAD && CONFIG_LIS2MDL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/lis2mdl/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2mdl/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2MDL 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS2MDL_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2MDL_TRIGGER_OWN_THREAD)、[`CONFIG_LIS2MDL`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2MDL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS2MDL_TRIGGER_GLOBAL_THREAD"></a>

## 156.85 `CONFIG_LIS2MDL_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LIS2MDL_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lis2mdl/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2mdl/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2MDL 磁力计（Magnetometer） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2MDL_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2MDL_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2MDL_TRIGGER`。

<a id="CONFIG_LIS2MDL_TRIGGER_MODE"></a>

## 156.86 `CONFIG_LIS2MDL_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS2MDL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_LIS2MDL_TRIGGER_GLOBAL_THREAD
```

**可选项（Choices）**

```text
CONFIG_LIS2MDL_TRIGGER_NONE
CONFIG_LIS2MDL_TRIGGER_GLOBAL_THREAD
CONFIG_LIS2MDL_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/lis2mdl/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2mdl/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2MDL 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS2MDL`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2MDL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LIS2MDL_TRIGGER_GLOBAL_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2MDL_TRIGGER_GLOBAL_THREAD)、[`CONFIG_LIS2MDL_TRIGGER_NONE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2MDL_TRIGGER_NONE)、[`CONFIG_LIS2MDL_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2MDL_TRIGGER_OWN_THREAD)。

<a id="CONFIG_LIS2MDL_TRIGGER_NONE"></a>

## 156.87 `CONFIG_LIS2MDL_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS2MDL_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/lis2mdl/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2mdl/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2MDL 磁力计（Magnetometer） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2MDL_TRIGGER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2MDL_TRIGGER_MODE)。

<a id="CONFIG_LIS2MDL_TRIGGER_OWN_THREAD"></a>

## 156.88 `CONFIG_LIS2MDL_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LIS2MDL_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lis2mdl/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2mdl/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS2MDL 磁力计（Magnetometer） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS2MDL_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS2MDL_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS2MDL_TRIGGER`。

<a id="CONFIG_LIS3MDL"></a>

## 156.89 `CONFIG_LIS3MDL`

**提示（Prompt）**：LIS3MDL 磁力计（Magnetometer）

**说明（Help）**

启用基于 I2C 的 LIS3MDL 磁力计（Magnetometer）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LIS3MDL_MAGN_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO if n
```

**定义位置（Location）**：[`drivers/sensor/st/lis3mdl/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis3mdl/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_LIS3MDL_FS"></a>

## 156.90 `CONFIG_LIS3MDL_FS`

**提示（Prompt）**：满量程范围（Full-scale Range）

**说明（Help）**

磁力计满量程范围（Magnetometer Full-scale Range）。配置值 X 表示范围为 ±X 高斯（Gauss）。有效值为 4、8、12 和 16。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS3MDL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/sensor/st/lis3mdl/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis3mdl/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS3MDL 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS3MDL`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS3MDL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS3MDL_ODR"></a>

## 156.91 `CONFIG_LIS3MDL_ODR`

**提示（Prompt）**：输出数据速率（Output Data Rate，ODR）

**说明（Help）**

磁力计输出数据速率（Output Data Rate），以每秒采样数表示。芯片支持的数据速率为 0.625、1.25、2.5、5、10、20、40、80、155、300、560 和 1000。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS3MDL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
"0.625"
```

**定义位置（Location）**：[`drivers/sensor/st/lis3mdl/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis3mdl/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS3MDL 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS3MDL`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS3MDL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS3MDL_THREAD_PRIORITY"></a>

## 156.92 `CONFIG_LIS3MDL_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS3MDL_TRIGGER_OWN_THREAD && CONFIG_LIS3MDL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/lis3mdl/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis3mdl/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS3MDL 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS3MDL_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS3MDL_TRIGGER_OWN_THREAD)、[`CONFIG_LIS3MDL`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS3MDL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS3MDL_THREAD_STACK_SIZE"></a>

## 156.93 `CONFIG_LIS3MDL_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS3MDL_TRIGGER_OWN_THREAD && CONFIG_LIS3MDL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/lis3mdl/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis3mdl/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS3MDL 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS3MDL_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS3MDL_TRIGGER_OWN_THREAD)、[`CONFIG_LIS3MDL`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS3MDL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LIS3MDL_TRIGGER_GLOBAL_THREAD"></a>

## 156.94 `CONFIG_LIS3MDL_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LIS3MDL_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lis3mdl/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis3mdl/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS3MDL 磁力计（Magnetometer） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS3MDL_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS3MDL_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS3MDL_TRIGGER`。

<a id="CONFIG_LIS3MDL_TRIGGER_MODE"></a>

## 156.95 `CONFIG_LIS3MDL_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIS3MDL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_LIS3MDL_TRIGGER_GLOBAL_THREAD
```

**可选项（Choices）**

```text
CONFIG_LIS3MDL_TRIGGER_NONE
CONFIG_LIS3MDL_TRIGGER_GLOBAL_THREAD
CONFIG_LIS3MDL_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/lis3mdl/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis3mdl/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS3MDL 磁力计（Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_LIS3MDL`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS3MDL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LIS3MDL_TRIGGER_GLOBAL_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS3MDL_TRIGGER_GLOBAL_THREAD)、[`CONFIG_LIS3MDL_TRIGGER_NONE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS3MDL_TRIGGER_NONE)、[`CONFIG_LIS3MDL_TRIGGER_OWN_THREAD`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS3MDL_TRIGGER_OWN_THREAD)。

<a id="CONFIG_LIS3MDL_TRIGGER_NONE"></a>

## 156.96 `CONFIG_LIS3MDL_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LIS3MDL_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/lis3mdl/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis3mdl/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS3MDL 磁力计（Magnetometer） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS3MDL_TRIGGER_MODE`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS3MDL_TRIGGER_MODE)。

<a id="CONFIG_LIS3MDL_TRIGGER_OWN_THREAD"></a>

## 156.97 `CONFIG_LIS3MDL_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LIS3MDL_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lis3mdl/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis3mdl/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LIS3MDL 磁力计（Magnetometer） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LIS3MDL_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIS3MDL_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LIS3MDL_TRIGGER`。

<a id="CONFIG_LM35"></a>

## 156.98 `CONFIG_LM35`

**提示（Prompt）**：LM35 温度传感器（Temperature Sensor）

**说明（Help）**

启用 LM35 温度传感器驱动；原文将其称为数字温度传感器（Digital Temperature Sensor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LM35_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/sensor/lm35/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/lm35/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_LM75"></a>

## 156.99 `CONFIG_LM75`

**提示（Prompt）**：LM75 温度传感器（Temperature Sensor）

**说明（Help）**

启用具有双线接口（2-wire Interface）的 LM75 数字温度传感器（Digital Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LM75_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/lm75/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/lm75/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_LM75_TRIGGER_GLOBAL_THREAD"></a>

## 156.100 `CONFIG_LM75_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LM75_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/lm75/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/lm75/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LM75 温度传感器（Temperature Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LM75_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LM75_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LM75_TRIGGER`。

<!-- kconfig-navigation -->

[上一章](P155_drivers_sensor_配置项参考_7.md) · [返回大纲](大纲.md) · [下一章](P157_drivers_sensor_配置项参考_9.md)
