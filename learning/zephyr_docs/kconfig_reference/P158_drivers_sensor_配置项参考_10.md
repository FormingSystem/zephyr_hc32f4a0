---
id: learning.zephyr-docs.kconfig-reference.page-158
title: "`drivers/sensor`配置项参考（10/15）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第158章\_`drivers/sensor`配置项参考（10/15）

本章翻译官方 Kconfig 数据库中 `drivers/sensor` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LSM6DSV16X_TRIGGER_GLOBAL_THREAD"></a>

## 158.1 `CONFIG_LSM6DSV16X_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_GPIO || CONFIG_I3C) && (n || n || n || n || n || n) && <choice CONFIG_LSM6DSV16X_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_LSM6DSV16X_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_LSM6DSV16X_TRIGGER_MODE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM6DSV16X_TRIGGER_MODE)、[`CONFIG_LSM6DSV16X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSV16X_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSV16X_TRIGGER`。

<a id="CONFIG_LSM6DSV16X_TRIGGER_MODE"></a>

## 158.2 `CONFIG_LSM6DSV16X_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSV16X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_LSM6DSV16X_TRIGGER_GLOBAL_THREAD if CONFIG_LSM6DSV16X_STREAM
CONFIG_LSM6DSV16X_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_LSM6DSV16X_TRIGGER_NONE
CONFIG_LSM6DSV16X_TRIGGER_GLOBAL_THREAD
CONFIG_LSM6DSV16X_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSV16X`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_LSM6DSV16X_TRIGGER_GLOBAL_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM6DSV16X_TRIGGER_GLOBAL_THREAD)、[`CONFIG_LSM6DSV16X_STREAM`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X_STREAM)、[`CONFIG_LSM6DSV16X_TRIGGER_NONE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM6DSV16X_TRIGGER_NONE)、[`CONFIG_LSM6DSV16X_TRIGGER_OWN_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM6DSV16X_TRIGGER_OWN_THREAD)。

<a id="CONFIG_LSM6DSV16X_TRIGGER_NONE"></a>

## 158.3 `CONFIG_LSM6DSV16X_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LSM6DSV16X_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSV16X_TRIGGER_MODE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM6DSV16X_TRIGGER_MODE)。

<a id="CONFIG_LSM6DSV16X_TRIGGER_OWN_THREAD"></a>

## 158.4 `CONFIG_LSM6DSV16X_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_GPIO || CONFIG_I3C) && (n || n || n || n || n || n) && <choice CONFIG_LSM6DSV16X_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_LSM6DSV16X_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_LSM6DSV16X_TRIGGER_MODE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM6DSV16X_TRIGGER_MODE)、[`CONFIG_LSM6DSV16X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSV16X_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSV16X_TRIGGER`。

<a id="CONFIG_LSM6DSVXXX"></a>

## 158.5 `CONFIG_LSM6DSVXXX`

**提示（Prompt）**：LSM6DSVXXX 惯性测量单元（IMU）传感器

**说明（Help）**

启用 LSM6DSVXXX 系列惯性测量单元（IMU）传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_LSM6DSV320X_ENABLED || DT_HAS_ST_LSM6DSV80X_ENABLED || DT_HAS_ST_ISM6HG256X_ENABLED) && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n || n || n
CONFIG_I3C if n || n || n
CONFIG_SPI if n || n || n
CONFIG_GPIO if n || n || n || n || n || n
CONFIG_I2C_RTIO if CONFIG_I2C && CONFIG_SENSOR_ASYNC_API
CONFIG_I3C_RTIO if CONFIG_I3C && CONFIG_SENSOR_ASYNC_API
CONFIG_SPI_RTIO if CONFIG_SPI && CONFIG_SENSOR_ASYNC_API
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_LSM6DSV320X if DT_HAS_ST_LSM6DSV320X_ENABLED
CONFIG_USE_STDC_LSM6DSV80X if DT_HAS_ST_LSM6DSV80X_ENABLED
CONFIG_USE_STDC_ISM6HG256X if DT_HAS_ST_ISM6HG256X_ENABLED
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsvxxx/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsvxxx/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_I3C_RTIO`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_RTIO)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_LSM6DSV320X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LSM6DSV320X)、[`CONFIG_USE_STDC_LSM6DSV80X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LSM6DSV80X)、[`CONFIG_USE_STDC_ISM6HG256X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_ISM6HG256X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_LSM6DSV320X`、`CONFIG_USE_STDC_LSM6DSV80X`、`CONFIG_USE_STDC_ISM6HG256X`。

<a id="CONFIG_LSM6DSVXXX_ENABLE_TEMP"></a>

## 158.6 `CONFIG_LSM6DSVXXX_ENABLE_TEMP`

**提示（Prompt）**：温度（Temperature）

**说明（Help）**

启用／禁用温度传感器（Temperature Sensor）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSVXXX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsvxxx/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsvxxx/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSVXXX 惯性测量单元（IMU）传感器

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSVXXX`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM6DSVXXX)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSVXXX_STREAM"></a>

## 158.7 `CONFIG_LSM6DSVXXX_STREAM`

**提示（Prompt）**：LSM6DSVXXX 数据流式传输（Data Streaming）

**说明（Help）**

使用此配置选项，启用通过实时 I/O（RTIO）子系统流式传输传感器数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SPI_RTIO || CONFIG_I2C_RTIO || CONFIG_I3C_RTIO) && CONFIG_SENSOR_ASYNC_API && CONFIG_LSM6DSVXXX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_LSM6DSVXXX_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsvxxx/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsvxxx/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSVXXX 惯性测量单元（IMU）传感器

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_I3C_RTIO`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_LSM6DSVXXX`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM6DSVXXX)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_LSM6DSVXXX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSVXXX_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSVXXX_TRIGGER`。

<a id="CONFIG_LSM9DS0_GYRO"></a>

## 158.8 `CONFIG_LSM9DS0_GYRO`

**提示（Prompt）**：LSM9DS0 I2C 陀螺仪芯片（Gyroscope Chip）

**说明（Help）**

启用基于 I2C 的 LSM9DS0 陀螺仪传感器（Gyroscope Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LSM9DS0_GYRO_ENABLED && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_gyro/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_gyro/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_LSM9DS0_GYRO_FULLSCALE_2000"></a>

## 158.9 `CONFIG_LSM9DS0_GYRO_FULLSCALE_2000`

**提示（Prompt）**：2000 度／秒（DPS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_gyro/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_gyro/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 陀螺仪芯片（Gyroscope Chip） → 属性（Attributes） → 默认满量程（Default Full-scale）

<a id="CONFIG_LSM9DS0_GYRO_FULLSCALE_245"></a>

## 158.10 `CONFIG_LSM9DS0_GYRO_FULLSCALE_245`

**提示（Prompt）**：245 度／秒（DPS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_gyro/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_gyro/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 陀螺仪芯片（Gyroscope Chip） → 属性（Attributes） → 默认满量程（Default Full-scale）

<a id="CONFIG_LSM9DS0_GYRO_FULLSCALE_500"></a>

## 158.11 `CONFIG_LSM9DS0_GYRO_FULLSCALE_500`

**提示（Prompt）**：500 度／秒（DPS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_gyro/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_gyro/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 陀螺仪芯片（Gyroscope Chip） → 属性（Attributes） → 默认满量程（Default Full-scale）

<a id="CONFIG_LSM9DS0_GYRO_FULLSCALE_RUNTIME"></a>

## 158.12 `CONFIG_LSM9DS0_GYRO_FULLSCALE_RUNTIME`

**提示（Prompt）**：动态满量程（Dynamic Full-scale）

**说明（Help）**

允许运行时修改满量程属性（Full-scale Attribute）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM9DS0_GYRO && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_gyro/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_gyro/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 陀螺仪芯片（Gyroscope Chip） → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM9DS0_GYRO`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_GYRO)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM9DS0_GYRO_SAMPLING_RATE_190"></a>

## 158.13 `CONFIG_LSM9DS0_GYRO_SAMPLING_RATE_190`

**提示（Prompt）**：190 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_gyro/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_gyro/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 陀螺仪芯片（Gyroscope Chip） → 属性（Attributes） → 默认采样频率（Default Sampling Rate Frequency）

<a id="CONFIG_LSM9DS0_GYRO_SAMPLING_RATE_380"></a>

## 158.14 `CONFIG_LSM9DS0_GYRO_SAMPLING_RATE_380`

**提示（Prompt）**：380 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_gyro/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_gyro/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 陀螺仪芯片（Gyroscope Chip） → 属性（Attributes） → 默认采样频率（Default Sampling Rate Frequency）

<a id="CONFIG_LSM9DS0_GYRO_SAMPLING_RATE_760"></a>

## 158.15 `CONFIG_LSM9DS0_GYRO_SAMPLING_RATE_760`

**提示（Prompt）**：760 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_gyro/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_gyro/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 陀螺仪芯片（Gyroscope Chip） → 属性（Attributes） → 默认采样频率（Default Sampling Rate Frequency）

<a id="CONFIG_LSM9DS0_GYRO_SAMPLING_RATE_95"></a>

## 158.16 `CONFIG_LSM9DS0_GYRO_SAMPLING_RATE_95`

**提示（Prompt）**：95 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_gyro/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_gyro/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 陀螺仪芯片（Gyroscope Chip） → 属性（Attributes） → 默认采样频率（Default Sampling Rate Frequency）

<a id="CONFIG_LSM9DS0_GYRO_SAMPLING_RATE_RUNTIME"></a>

## 158.17 `CONFIG_LSM9DS0_GYRO_SAMPLING_RATE_RUNTIME`

**提示（Prompt）**：动态采样率（Dynamic Sampling Rate）

**说明（Help）**

允许运行时修改采样频率（Sampling Rate Frequency）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM9DS0_GYRO && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_gyro/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_gyro/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 陀螺仪芯片（Gyroscope Chip） → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM9DS0_GYRO`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_GYRO)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM9DS0_GYRO_THREAD_STACK_SIZE"></a>

## 158.18 `CONFIG_LSM9DS0_GYRO_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

指定内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM9DS0_GYRO_TRIGGERS && CONFIG_LSM9DS0_GYRO && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_gyro/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_gyro/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 陀螺仪芯片（Gyroscope Chip） → 触发器（Triggers）

**配置项引用（Symbol References）**：[`CONFIG_LSM9DS0_GYRO_TRIGGERS`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_GYRO_TRIGGERS)、[`CONFIG_LSM9DS0_GYRO`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_GYRO)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM9DS0_GYRO_TRIGGERS"></a>

## 158.19 `CONFIG_LSM9DS0_GYRO_TRIGGERS`

**提示（Prompt）**：触发器（Triggers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_gyro/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_gyro/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 陀螺仪芯片（Gyroscope Chip）

<a id="CONFIG_LSM9DS0_GYRO_TRIGGER_DRDY"></a>

## 158.20 `CONFIG_LSM9DS0_GYRO_TRIGGER_DRDY`

**提示（Prompt）**：数据就绪触发（Data Ready Trigger）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM9DS0_GYRO_TRIGGERS && CONFIG_LSM9DS0_GYRO && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_gyro/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_gyro/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 陀螺仪芯片（Gyroscope Chip） → 触发器（Triggers）

**配置项引用（Symbol References）**：[`CONFIG_LSM9DS0_GYRO_TRIGGERS`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_GYRO_TRIGGERS)、[`CONFIG_LSM9DS0_GYRO`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_GYRO)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM9DS0_MFD"></a>

## 158.21 `CONFIG_LSM9DS0_MFD`

**提示（Prompt）**：LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片

**说明（Help）**

启用基于 I2C 的 LSM9DS0 多功能器件（MFD）传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LSM9DS0_MFD_ENABLED && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_LSM9DS0_MFD_ACCEL_ENABLE"></a>

## 158.22 `CONFIG_LSM9DS0_MFD_ACCEL_ENABLE`

**提示（Prompt）**：加速度计（Accelerometer）

**说明（Help）**

启用／禁用加速度计；禁用时，从驱动中移除全部加速度计相关内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM9DS0_MFD && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM9DS0_MFD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM9DS0_MFD_ACCEL_ENABLE_X"></a>

## 158.23 `CONFIG_LSM9DS0_MFD_ACCEL_ENABLE_X`

**提示（Prompt）**：加速度计 X 轴（Accelerometer X Axis）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM9DS0_MFD_ACCEL_ENABLE && CONFIG_LSM9DS0_MFD && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM9DS0_MFD_ACCEL_ENABLE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD_ACCEL_ENABLE)、[`CONFIG_LSM9DS0_MFD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM9DS0_MFD_ACCEL_ENABLE_Y"></a>

## 158.24 `CONFIG_LSM9DS0_MFD_ACCEL_ENABLE_Y`

**提示（Prompt）**：加速度计 Y 轴（Accelerometer Y Axis）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM9DS0_MFD_ACCEL_ENABLE && CONFIG_LSM9DS0_MFD && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM9DS0_MFD_ACCEL_ENABLE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD_ACCEL_ENABLE)、[`CONFIG_LSM9DS0_MFD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM9DS0_MFD_ACCEL_ENABLE_Z"></a>

## 158.25 `CONFIG_LSM9DS0_MFD_ACCEL_ENABLE_Z`

**提示（Prompt）**：加速度计 Z 轴（Accelerometer Z Axis）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM9DS0_MFD_ACCEL_ENABLE && CONFIG_LSM9DS0_MFD && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM9DS0_MFD_ACCEL_ENABLE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD_ACCEL_ENABLE)、[`CONFIG_LSM9DS0_MFD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM9DS0_MFD_ACCEL_FULL_SCALE_16"></a>

## 158.26 `CONFIG_LSM9DS0_MFD_ACCEL_FULL_SCALE_16`

**提示（Prompt）**：16G

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计满量程（Accelerometer Full-scale）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_FULL_SCALE_2"></a>

## 158.27 `CONFIG_LSM9DS0_MFD_ACCEL_FULL_SCALE_2`

**提示（Prompt）**：第二代移动通信（2G）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计满量程（Accelerometer Full-scale）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_FULL_SCALE_4"></a>

## 158.28 `CONFIG_LSM9DS0_MFD_ACCEL_FULL_SCALE_4`

**提示（Prompt）**：第四代移动通信（4G）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计满量程（Accelerometer Full-scale）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_FULL_SCALE_6"></a>

## 158.29 `CONFIG_LSM9DS0_MFD_ACCEL_FULL_SCALE_6`

**提示（Prompt）**：6 G

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计满量程（Accelerometer Full-scale）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_FULL_SCALE_8"></a>

## 158.30 `CONFIG_LSM9DS0_MFD_ACCEL_FULL_SCALE_8`

**提示（Prompt）**：8G

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计满量程（Accelerometer Full-scale）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_FULL_SCALE_RUNTIME"></a>

## 158.31 `CONFIG_LSM9DS0_MFD_ACCEL_FULL_SCALE_RUNTIME`

**提示（Prompt）**：加速度计动态满量程（Dynamic Full-scale）

**说明（Help）**

允许运行时修改加速度计满量程属性（Full-scale Attribute）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM9DS0_MFD_ACCEL_ENABLE && CONFIG_LSM9DS0_MFD && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM9DS0_MFD_ACCEL_ENABLE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD_ACCEL_ENABLE)、[`CONFIG_LSM9DS0_MFD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_0"></a>

## 158.32 `CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_0`

**提示（Prompt）**：0 Hz（掉电，Power Down）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计采样率（Accelerometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_100"></a>

## 158.33 `CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_100`

**提示（Prompt）**：频率：100 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计采样率（Accelerometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_12_5"></a>

## 158.34 `CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_12_5`

**提示（Prompt）**：频率：12.5 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计采样率（Accelerometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_1600"></a>

## 158.35 `CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_1600`

**提示（Prompt）**：频率：1600 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计采样率（Accelerometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_200"></a>

## 158.36 `CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_200`

**提示（Prompt）**：频率：200 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计采样率（Accelerometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_25"></a>

## 158.37 `CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_25`

**提示（Prompt）**：频率：25 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计采样率（Accelerometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_3_125"></a>

## 158.38 `CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_3_125`

**提示（Prompt）**：频率（Frequency）：3.125 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计采样率（Accelerometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_400"></a>

## 158.39 `CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_400`

**提示（Prompt）**：频率：400 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计采样率（Accelerometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_50"></a>

## 158.40 `CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_50`

**提示（Prompt）**：频率：50 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计采样率（Accelerometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_6_25"></a>

## 158.41 `CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_6_25`

**提示（Prompt）**：频率：6.25 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计采样率（Accelerometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_800"></a>

## 158.42 `CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_800`

**提示（Prompt）**：频率：800 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 加速度计采样率（Accelerometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_RUNTIME"></a>

## 158.43 `CONFIG_LSM9DS0_MFD_ACCEL_SAMPLING_RATE_RUNTIME`

**提示（Prompt）**：加速度计动态采样率（Dynamic Sampling Rate）

**说明（Help）**

允许运行时修改加速度计采样率属性（Sampling Rate Attribute）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM9DS0_MFD_ACCEL_ENABLE && CONFIG_LSM9DS0_MFD && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM9DS0_MFD_ACCEL_ENABLE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD_ACCEL_ENABLE)、[`CONFIG_LSM9DS0_MFD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM9DS0_MFD_MAGN_ENABLE"></a>

## 158.44 `CONFIG_LSM9DS0_MFD_MAGN_ENABLE`

**提示（Prompt）**：磁力计（Magnetometer）

**说明（Help）**

启用／禁用磁力计；禁用时，从驱动中移除全部磁力计相关内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM9DS0_MFD && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM9DS0_MFD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM9DS0_MFD_MAGN_FULL_SCALE_12"></a>

## 158.45 `CONFIG_LSM9DS0_MFD_MAGN_FULL_SCALE_12`

**提示（Prompt）**：12 高斯（Gauss）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L184)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 磁力计满量程（Magnetometer Full-scale）

<a id="CONFIG_LSM9DS0_MFD_MAGN_FULL_SCALE_2"></a>

## 158.46 `CONFIG_LSM9DS0_MFD_MAGN_FULL_SCALE_2`

**提示（Prompt）**：2 高斯（Gauss）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 磁力计满量程（Magnetometer Full-scale）

<a id="CONFIG_LSM9DS0_MFD_MAGN_FULL_SCALE_4"></a>

## 158.47 `CONFIG_LSM9DS0_MFD_MAGN_FULL_SCALE_4`

**提示（Prompt）**：4 高斯（Gauss）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 磁力计满量程（Magnetometer Full-scale）

<a id="CONFIG_LSM9DS0_MFD_MAGN_FULL_SCALE_8"></a>

## 158.48 `CONFIG_LSM9DS0_MFD_MAGN_FULL_SCALE_8`

**提示（Prompt）**：8 高斯（Gauss）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 磁力计满量程（Magnetometer Full-scale）

<a id="CONFIG_LSM9DS0_MFD_MAGN_FULL_SCALE_RUNTIME"></a>

## 158.49 `CONFIG_LSM9DS0_MFD_MAGN_FULL_SCALE_RUNTIME`

**提示（Prompt）**：磁力计动态满量程（Dynamic Full-scale）

**说明（Help）**

允许运行时修改磁力计满量程属性（Full-scale Attribute）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM9DS0_MFD_MAGN_ENABLE && CONFIG_LSM9DS0_MFD && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM9DS0_MFD_MAGN_ENABLE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD_MAGN_ENABLE)、[`CONFIG_LSM9DS0_MFD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM9DS0_MFD_MAGN_SAMPLING_RATE_100"></a>

## 158.50 `CONFIG_LSM9DS0_MFD_MAGN_SAMPLING_RATE_100`

**提示（Prompt）**：频率：100 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L156)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 磁力计采样率（Magnetometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_MAGN_SAMPLING_RATE_12_5"></a>

## 158.51 `CONFIG_LSM9DS0_MFD_MAGN_SAMPLING_RATE_12_5`

**提示（Prompt）**：频率：12.5 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L147)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 磁力计采样率（Magnetometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_MAGN_SAMPLING_RATE_25"></a>

## 158.52 `CONFIG_LSM9DS0_MFD_MAGN_SAMPLING_RATE_25`

**提示（Prompt）**：频率：25 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 磁力计采样率（Magnetometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_MAGN_SAMPLING_RATE_3_125"></a>

## 158.53 `CONFIG_LSM9DS0_MFD_MAGN_SAMPLING_RATE_3_125`

**提示（Prompt）**：频率（Frequency）：3.125 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 磁力计采样率（Magnetometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_MAGN_SAMPLING_RATE_50"></a>

## 158.54 `CONFIG_LSM9DS0_MFD_MAGN_SAMPLING_RATE_50`

**提示（Prompt）**：频率：50 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 磁力计采样率（Magnetometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_MAGN_SAMPLING_RATE_6_25"></a>

## 158.55 `CONFIG_LSM9DS0_MFD_MAGN_SAMPLING_RATE_6_25`

**提示（Prompt）**：频率：6.25 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes） → 磁力计采样率（Magnetometer Sampling Rate）

<a id="CONFIG_LSM9DS0_MFD_MAGN_SAMPLING_RATE_RUNTIME"></a>

## 158.56 `CONFIG_LSM9DS0_MFD_MAGN_SAMPLING_RATE_RUNTIME`

**提示（Prompt）**：磁力计动态采样率（Dynamic Sampling Rate）

**说明（Help）**

允许运行时修改磁力计采样率属性（Sampling Rate Attribute）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM9DS0_MFD_MAGN_ENABLE && CONFIG_LSM9DS0_MFD && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM9DS0_MFD_MAGN_ENABLE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD_MAGN_ENABLE)、[`CONFIG_LSM9DS0_MFD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM9DS0_MFD_TEMP_ENABLE"></a>

## 158.57 `CONFIG_LSM9DS0_MFD_TEMP_ENABLE`

**提示（Prompt）**：温度传感器（Temperature Sensor）

**说明（Help）**

启用／禁用温度传感器；禁用时，从驱动中移除全部温度传感器相关内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM9DS0_MFD && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds0_mfd/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds0_mfd/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS0 I2C 加速度计、磁力计与温度传感器芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM9DS0_MFD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS0_MFD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM9DS1"></a>

## 158.58 `CONFIG_LSM9DS1`

**提示（Prompt）**：LSM9DS1 I2C 加速度计与陀螺仪芯片

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LSM9DS1_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_LSM9DS1
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds1/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds1/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_LSM9DS1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LSM9DS1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_LSM9DS1`。

<a id="CONFIG_LSM9DS1_ENABLE_TEMP"></a>

## 158.59 `CONFIG_LSM9DS1_ENABLE_TEMP`

**提示（Prompt）**：LSM9DS1 温度传感器（Temperature Sensor）

**说明（Help）**

启用／禁用温度功能

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM9DS1 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds1/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds1/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM9DS1 I2C 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM9DS1`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM9DS1)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_LSM9DS1_MAG"></a>

## 158.60 `CONFIG_LSM9DS1_MAG`

**提示（Prompt）**：LSM9DS1 I2C 磁力计芯片（Magnetometer Chip）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LSM9DS1_MAG_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_LSM9DS1
```

**定义位置（Location）**：[`drivers/sensor/st/lsm9ds1_mag/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds1_mag/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_LSM9DS1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LSM9DS1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_LSM9DS1`。

<a id="CONFIG_LTC4286"></a>

## 158.61 `CONFIG_LTC4286`

**提示（Prompt）**：LTC4286 功率监测器（Power Monitor）

**说明（Help）**

启用 Analog Devices LTC4286 驱动，该器件是带功率监测器（Power Monitor）的大功率正电源热插拔控制器（High Power Positive Hot-Swap Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_LTC4286_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/adi/ltc4286/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/ltc4286/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_LTC4286_THREAD_PRIORITY"></a>

## 158.62 `CONFIG_LTC4286_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LTC4286_TRIGGER_OWN_THREAD && CONFIG_LTC4286_TRIGGER && CONFIG_LTC4286 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/adi/ltc4286/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/ltc4286/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LTC4286 功率监测器（Power Monitor）

**配置项引用（Symbol References）**：[`CONFIG_LTC4286_TRIGGER_OWN_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LTC4286_TRIGGER_OWN_THREAD)、[`CONFIG_LTC4286_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LTC4286_TRIGGER)、[`CONFIG_LTC4286`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LTC4286)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LTC4286_TRIGGER`。

<a id="CONFIG_LTC4286_THREAD_STACK_SIZE"></a>

## 158.63 `CONFIG_LTC4286_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

分配给驱动中断处理线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LTC4286_TRIGGER_OWN_THREAD && CONFIG_LTC4286_TRIGGER && CONFIG_LTC4286 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/adi/ltc4286/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/ltc4286/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LTC4286 功率监测器（Power Monitor）

**配置项引用（Symbol References）**：[`CONFIG_LTC4286_TRIGGER_OWN_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LTC4286_TRIGGER_OWN_THREAD)、[`CONFIG_LTC4286_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LTC4286_TRIGGER)、[`CONFIG_LTC4286`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LTC4286)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LTC4286_TRIGGER`。

<a id="CONFIG_LTC4286_TRIGGER_GLOBAL_THREAD"></a>

## 158.64 `CONFIG_LTC4286_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && CONFIG_LTC4286_HAS_TRIGGER_GPIO && <choice>
```

**主动选择（Selects）**

```text
CONFIG_LTC4286_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/ltc4286/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/ltc4286/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LTC4286 功率监测器（Power Monitor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_LTC4286_HAS_TRIGGER_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LTC4286_HAS_TRIGGER_GPIO)、[`CONFIG_LTC4286_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LTC4286_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LTC4286_HAS_TRIGGER_GPIO`、`CONFIG_LTC4286_TRIGGER`。

<a id="CONFIG_LTC4286_TRIGGER_NONE"></a>

## 158.65 `CONFIG_LTC4286_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/adi/ltc4286/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/ltc4286/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LTC4286 功率监测器（Power Monitor） → 触发模式（Trigger Mode）

<a id="CONFIG_LTC4286_TRIGGER_OWN_THREAD"></a>

## 158.66 `CONFIG_LTC4286_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用自身分配的线程（Thread Allocated to Self）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && CONFIG_LTC4286_HAS_TRIGGER_GPIO && <choice>
```

**主动选择（Selects）**

```text
CONFIG_LTC4286_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/ltc4286/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/ltc4286/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LTC4286 功率监测器（Power Monitor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_LTC4286_HAS_TRIGGER_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LTC4286_HAS_TRIGGER_GPIO)、[`CONFIG_LTC4286_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LTC4286_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LTC4286_HAS_TRIGGER_GPIO`、`CONFIG_LTC4286_TRIGGER`。

<a id="CONFIG_LTR55X"></a>

## 158.67 `CONFIG_LTR55X`

**提示（Prompt）**：LiteOn LTR-329/LTR-553 环境光／接近传感器支持

**说明（Help）**

启用 Lite-On LTR-329 环境光传感器（Ambient Light Sensor）和 LTR-55X 环境光与接近传感器（Ambient Light and Proximity Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_LITEON_LTR329_ENABLED || DT_HAS_LITEON_LTR553_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/liteon/ltr55x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/liteon/ltr55x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_LTR_F216A"></a>

## 158.68 `CONFIG_LTR_F216A`

**提示（Prompt）**：LiteOn LTR-F216A 光照传感器（Light Sensor）

**说明（Help）**

启用 LiteOn LTR-F216A 光照传感器（Light Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEON_LTRF216A_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/liteon/ltrf216a/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/liteon/ltrf216a/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MAX17055"></a>

## 158.69 `CONFIG_MAX17055`

**提示（Prompt）**：MAX17055 电量计（Fuel Gauge）

**说明（Help）**

启用基于 I2C 的 MAX17055 电量计（Fuel Gauge）驱动。此驱动支持读取多种传感器设置，包括电量百分比、充满／耗尽所需时间、设计电压、温度和剩余容量。

译注：原文将剩余容量的单位写为 mA；此处保留该单位说明，不将它擅自改成 mAh。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX17055_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/maxim/max17055/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max17055/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MAX17262"></a>

## 158.70 `CONFIG_MAX17262`

**提示（Prompt）**：MAX17262 电量计（Fuel Gauge）

**说明（Help）**

启用基于 I2C 的 MAX17262 电量计（Fuel Gauge）驱动。此驱动支持读取多种传感器设置，包括电压、电流、温度、充满／耗尽所需时间，以及以 mAh 表示的剩余容量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX17262_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/maxim/max17262/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max17262/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MAX30009"></a>

## 158.71 `CONFIG_MAX30009`

**提示（Prompt）**：MAX30009 生物阻抗模拟前端（Bio-Impedance AFE）

**说明（Help）**

启用 MAX30009 生物阻抗模拟前端（Bio-Impedance Analog Front End，AFE）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX30009_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_RTIO_WORKQ if CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/adi/max30009/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30009/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_MAX30009_INIT_PRIORITY"></a>

## 158.72 `CONFIG_MAX30009_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

MAX30009 驱动的初始化优先级（Initialization Priority）。原文要求它低于任何需要使用该驱动的线程的优先级。

译注：原文在此将初始化优先级与线程优先级进行比较；两类优先级的含义应结合 Zephyr 初始化流程和线程调度规则分别理解。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MAX30009 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_SENSOR_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/sensor/adi/max30009/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30009/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30009 生物阻抗模拟前端（Bio-Impedance AFE）

**配置项引用（Symbol References）**：[`CONFIG_MAX30009`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30009)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SENSOR_INIT_PRIORITY`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_INIT_PRIORITY)。

<a id="CONFIG_MAX30009_STREAM"></a>

## 158.73 `CONFIG_MAX30009_STREAM`

**提示（Prompt）**：使用流式模式（Streaming Mode）

**说明（Help）**

使用此配置选项启用通过 RTIO 流式传输传感器数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MAX30009 && CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_MAX30009_TRIGGER
CONFIG_SPI_RTIO if n
CONFIG_I2C_RTIO if n
CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/adi/max30009/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30009/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30009 生物阻抗模拟前端（Bio-Impedance AFE）

**配置项引用（Symbol References）**：[`CONFIG_MAX30009`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30009)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_MAX30009_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX30009_TRIGGER)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MAX30009_TRIGGER`。

<a id="CONFIG_MAX30009_THREAD_PRIORITY"></a>

## 158.74 `CONFIG_MAX30009_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MAX30009_TRIGGER_OWN_THREAD && CONFIG_MAX30009_TRIGGER && CONFIG_MAX30009 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/adi/max30009/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30009/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30009 生物阻抗模拟前端（Bio-Impedance AFE）

**配置项引用（Symbol References）**：[`CONFIG_MAX30009_TRIGGER_OWN_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30009_TRIGGER_OWN_THREAD)、[`CONFIG_MAX30009_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX30009_TRIGGER)、[`CONFIG_MAX30009`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30009)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MAX30009_TRIGGER`。

<a id="CONFIG_MAX30009_THREAD_STACK_SIZE"></a>

## 158.75 `CONFIG_MAX30009_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MAX30009_TRIGGER_OWN_THREAD && CONFIG_MAX30009_TRIGGER && CONFIG_MAX30009 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/sensor/adi/max30009/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30009/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30009 生物阻抗模拟前端（Bio-Impedance AFE）

**配置项引用（Symbol References）**：[`CONFIG_MAX30009_TRIGGER_OWN_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30009_TRIGGER_OWN_THREAD)、[`CONFIG_MAX30009_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX30009_TRIGGER)、[`CONFIG_MAX30009`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30009)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MAX30009_TRIGGER`。

<a id="CONFIG_MAX30009_TRIGGER_GLOBAL_THREAD"></a>

## 158.76 `CONFIG_MAX30009_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MAX30009_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_MAX30009_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/max30009/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30009/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30009 生物阻抗模拟前端（Bio-Impedance AFE） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_MAX30009_TRIGGER_MODE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30009_TRIGGER_MODE)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MAX30009_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX30009_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MAX30009_TRIGGER`。

<a id="CONFIG_MAX30009_TRIGGER_MODE"></a>

## 158.77 `CONFIG_MAX30009_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MAX30009 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_MAX30009_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_MAX30009_TRIGGER_NONE
CONFIG_MAX30009_TRIGGER_GLOBAL_THREAD
CONFIG_MAX30009_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/adi/max30009/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30009/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30009 生物阻抗模拟前端（Bio-Impedance AFE）

**配置项引用（Symbol References）**：[`CONFIG_MAX30009`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30009)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_MAX30009_TRIGGER_NONE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30009_TRIGGER_NONE)、[`CONFIG_MAX30009_TRIGGER_GLOBAL_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30009_TRIGGER_GLOBAL_THREAD)、[`CONFIG_MAX30009_TRIGGER_OWN_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30009_TRIGGER_OWN_THREAD)。

<a id="CONFIG_MAX30009_TRIGGER_NONE"></a>

## 158.78 `CONFIG_MAX30009_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MAX30009_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/adi/max30009/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30009/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30009 生物阻抗模拟前端（Bio-Impedance AFE） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_MAX30009_TRIGGER_MODE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30009_TRIGGER_MODE)。

<a id="CONFIG_MAX30009_TRIGGER_OWN_THREAD"></a>

## 158.79 `CONFIG_MAX30009_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MAX30009_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_MAX30009_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/max30009/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30009/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30009 生物阻抗模拟前端（Bio-Impedance AFE） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_MAX30009_TRIGGER_MODE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30009_TRIGGER_MODE)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MAX30009_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX30009_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MAX30009_TRIGGER`。

<a id="CONFIG_MAX30101"></a>

## 158.80 `CONFIG_MAX30101`

**提示（Prompt）**：MAX30101 脉搏血氧计与心率传感器（Pulse Oximeter and Heart Rate Sensor）

**说明（Help）**

启用 MAX30101/MAX30102 系列心率与脉搏血氧传感器（Heart Rate and Pulse Oximeter Sensor）驱动。MAX30102 与 MAX30101 寄存器兼容，但只有红光和红外（IR）LED 通道，没有绿光 LED。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_MAXIM_MAX30101_ENABLED || DT_HAS_MAXIM_MAX30102_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_I2C if n
```

**定义位置（Location）**：[`drivers/sensor/maxim/max30101/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max30101/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MAX30101_DIE_TEMPERATURE"></a>

## 158.81 `CONFIG_MAX30101_DIE_TEMPERATURE`

**提示（Prompt）**：芯片裸片温度采集（Die Temperature Acquisition）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MAX30101 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/maxim/max30101/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max30101/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30101 脉搏血氧计与心率传感器（Pulse Oximeter and Heart Rate Sensor）

**配置项引用（Symbol References）**：[`CONFIG_MAX30101`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30101)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MAX30101_THREAD_PRIORITY"></a>

## 158.82 `CONFIG_MAX30101_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MAX30101_TRIGGER_OWN_THREAD && CONFIG_MAX30101_TRIGGER && CONFIG_MAX30101 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/maxim/max30101/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max30101/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30101 脉搏血氧计与心率传感器（Pulse Oximeter and Heart Rate Sensor）

**配置项引用（Symbol References）**：[`CONFIG_MAX30101_TRIGGER_OWN_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30101_TRIGGER_OWN_THREAD)、[`CONFIG_MAX30101_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX30101_TRIGGER)、[`CONFIG_MAX30101`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30101)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MAX30101_TRIGGER`。

<a id="CONFIG_MAX30101_THREAD_SIZE"></a>

## 158.83 `CONFIG_MAX30101_THREAD_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MAX30101_TRIGGER_OWN_THREAD && CONFIG_MAX30101_TRIGGER && CONFIG_MAX30101 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/sensor/maxim/max30101/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max30101/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30101 脉搏血氧计与心率传感器（Pulse Oximeter and Heart Rate Sensor）

**配置项引用（Symbol References）**：[`CONFIG_MAX30101_TRIGGER_OWN_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30101_TRIGGER_OWN_THREAD)、[`CONFIG_MAX30101_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX30101_TRIGGER)、[`CONFIG_MAX30101`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30101)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MAX30101_TRIGGER`。

<a id="CONFIG_MAX30101_TRIGGER_GLOBAL_THREAD"></a>

## 158.84 `CONFIG_MAX30101_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && (n || n) && <choice CONFIG_MAX30101_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MAX30101_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/maxim/max30101/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max30101/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30101 脉搏血氧计与心率传感器（Pulse Oximeter and Heart Rate Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MAX30101_TRIGGER_MODE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30101_TRIGGER_MODE)、[`CONFIG_MAX30101_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX30101_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MAX30101_TRIGGER`。

<a id="CONFIG_MAX30101_TRIGGER_MODE"></a>

## 158.85 `CONFIG_MAX30101_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MAX30101 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_MAX30101_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_MAX30101_TRIGGER_NONE
CONFIG_MAX30101_TRIGGER_GLOBAL_THREAD
CONFIG_MAX30101_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/maxim/max30101/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max30101/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30101 脉搏血氧计与心率传感器（Pulse Oximeter and Heart Rate Sensor）

**配置项引用（Symbol References）**：[`CONFIG_MAX30101`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30101)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_MAX30101_TRIGGER_NONE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30101_TRIGGER_NONE)、[`CONFIG_MAX30101_TRIGGER_GLOBAL_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30101_TRIGGER_GLOBAL_THREAD)、[`CONFIG_MAX30101_TRIGGER_OWN_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30101_TRIGGER_OWN_THREAD)。

<a id="CONFIG_MAX30101_TRIGGER_NONE"></a>

## 158.86 `CONFIG_MAX30101_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MAX30101_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/maxim/max30101/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max30101/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30101 脉搏血氧计与心率传感器（Pulse Oximeter and Heart Rate Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_MAX30101_TRIGGER_MODE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30101_TRIGGER_MODE)。

<a id="CONFIG_MAX30101_TRIGGER_OWN_THREAD"></a>

## 158.87 `CONFIG_MAX30101_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && (n || n) && <choice CONFIG_MAX30101_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MAX30101_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/maxim/max30101/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max30101/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30101 脉搏血氧计与心率传感器（Pulse Oximeter and Heart Rate Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MAX30101_TRIGGER_MODE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30101_TRIGGER_MODE)、[`CONFIG_MAX30101_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX30101_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MAX30101_TRIGGER`。

<a id="CONFIG_MAX30210"></a>

## 158.88 `CONFIG_MAX30210`

**提示（Prompt）**：MAX30210 温度传感器（Temperature Sensor）

**说明（Help）**

启用 MAX30210 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX30210_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/adi/max30210/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30210/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MAX30210_THREAD_PRIORITY"></a>

## 158.89 `CONFIG_MAX30210_THREAD_PRIORITY`

**提示（Prompt）**：中断处理程序的线程优先级（Thread Priority）

**说明（Help）**

中断处理线程（Interrupt Handler Thread）的优先级。原文说明数字越大，优先级越高。该线程是协作式（Cooperative）线程，在主动让出执行权之前，不会被另一个线程打断。

译注：这里保留上游对数值方向的说明；实际使用应对照驱动的优先级换算，不应将此句视为所有 Zephyr 线程优先级的通用规则。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MAX30210_TRIGGER_OWN_THREAD && CONFIG_MAX30210 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/adi/max30210/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30210/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30210 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_MAX30210_TRIGGER_OWN_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30210_TRIGGER_OWN_THREAD)、[`CONFIG_MAX30210`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30210)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MAX30210_THREAD_STACK_SIZE"></a>

## 158.90 `CONFIG_MAX30210_THREAD_STACK_SIZE`

**提示（Prompt）**：中断处理线程栈大小（Stack Size）

**说明（Help）**

中断处理线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MAX30210_TRIGGER_OWN_THREAD && CONFIG_MAX30210 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/adi/max30210/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30210/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30210 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_MAX30210_TRIGGER_OWN_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30210_TRIGGER_OWN_THREAD)、[`CONFIG_MAX30210`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30210)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MAX30210_TRIGGER_GLOBAL_THREAD"></a>

## 158.91 `CONFIG_MAX30210_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**

使用全局线程（Global Thread）处理中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_MAX30210_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/max30210/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30210/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30210 温度传感器（Temperature Sensor） → 设置触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MAX30210_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX30210_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MAX30210_TRIGGER`。

<a id="CONFIG_MAX30210_TRIGGER_MODE"></a>

## 158.92 `CONFIG_MAX30210_TRIGGER_MODE`

**提示（Prompt）**：设置触发模式（Trigger Mode）

**说明（Help）**

设置中断处理程序使用的线程类型。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MAX30210 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_MAX30210_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_MAX30210_TRIGGER_NONE
CONFIG_MAX30210_TRIGGER_GLOBAL_THREAD
CONFIG_MAX30210_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/adi/max30210/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30210/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30210 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_MAX30210`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30210)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_MAX30210_TRIGGER_NONE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30210_TRIGGER_NONE)、[`CONFIG_MAX30210_TRIGGER_GLOBAL_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30210_TRIGGER_GLOBAL_THREAD)、[`CONFIG_MAX30210_TRIGGER_OWN_THREAD`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30210_TRIGGER_OWN_THREAD)。

<a id="CONFIG_MAX30210_TRIGGER_NONE"></a>

## 158.93 `CONFIG_MAX30210_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MAX30210_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/adi/max30210/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30210/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30210 温度传感器（Temperature Sensor） → 设置触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_MAX30210_TRIGGER_MODE`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30210_TRIGGER_MODE)。

<a id="CONFIG_MAX30210_TRIGGER_OWN_THREAD"></a>

## 158.94 `CONFIG_MAX30210_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**

使用独立线程（Separate Thread）处理中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_MAX30210_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/max30210/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30210/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX30210 温度传感器（Temperature Sensor） → 设置触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MAX30210_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX30210_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MAX30210_TRIGGER`。

<a id="CONFIG_MAX31790_FAN_FAULT"></a>

## 158.95 `CONFIG_MAX31790_FAN_FAULT`

**提示（Prompt）**：MAX31790 风扇故障传感器（Fan Fault Sensor）

**说明（Help）**

启用 MAX31790 风扇故障传感器（Fan Fault Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX31790_FAN_FAULT_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/sensor/maxim/max31790/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max31790/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MAX31790_FAN_SPEED"></a>

## 158.96 `CONFIG_MAX31790_FAN_SPEED`

**提示（Prompt）**：MAX31790 风扇转速传感器（Fan Speed Sensor）

**说明（Help）**

启用 MAX31790 风扇转速传感器（Fan Speed Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX31790_FAN_SPEED_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/sensor/maxim/max31790/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max31790/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_MAX31790_SENSOR"></a>

## 158.97 `CONFIG_MAX31790_SENSOR`

**提示（Prompt）**：MAX31790 传感器（Sensors）

**说明（Help）**

启用 MAX31790 脉宽调制（PWM）控制器的传感器功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_MAX31790_FAN_SPEED || CONFIG_MAX31790_FAN_FAULT) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/maxim/max31790/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max31790/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MAX31790_FAN_SPEED`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX31790_FAN_SPEED)、[`CONFIG_MAX31790_FAN_FAULT`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX31790_FAN_FAULT)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MAX31826"></a>

## 158.98 `CONFIG_MAX31826`

**提示（Prompt）**：MAX31826 单总线温度传感器（1-Wire Temperature Sensor）

**说明（Help）**

启用 MAX31826 单总线温度传感器（1-Wire Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX31826_ENABLED && CONFIG_W1_NET && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/maxim/max31826/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max31826/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_W1_NET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_W1_NET)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MAX31855"></a>

## 158.99 `CONFIG_MAX31855`

**提示（Prompt）**：MAX31855 传感器（Sensor）

**说明（Help）**

启用基于 SPI、带冷端补偿（Cold-Junction Compensation）的 MAX31855 热电偶数字转换器（Thermocouple-to-Digital Converter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX31855_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/sensor/maxim/max31855/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max31855/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_MAX31865"></a>

## 158.100 `CONFIG_MAX31865`

**提示（Prompt）**：MAX31865 温度传感器（Temperature Sensor）

**说明（Help）**

启用 Maxim MAX31865 SPI 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX31865_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/sensor/maxim/max31865/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max31865/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<!-- kconfig-navigation -->

[上一章](P157_drivers_sensor_配置项参考_9.md) · [返回大纲](大纲.md) · [下一章](P159_drivers_sensor_配置项参考_11.md)
