---
id: learning.zephyr-docs.kconfig-reference.page-159
title: "`drivers/sensor`配置项参考（11/15）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第159章\_`drivers/sensor`配置项参考（11/15）

本章翻译官方 Kconfig 数据库中 `drivers/sensor` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MAX31875"></a>

## 159.1 `CONFIG_MAX31875`

**提示（Prompt）**：MAX31875 温度传感器（Temperature Sensor）

**说明（Help）**

启用 Maxim MAX31875 低功耗 I2C 温度传感器（Low-Power Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX31875_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/maxim/max31875/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max31875/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MAX32664C_QUEUE_SIZE"></a>

## 159.2 `CONFIG_MAX32664C_QUEUE_SIZE`

**提示（Prompt）**：消息队列（Message Queue）长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR_MAX32664C && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/sensor/adi/max32664c/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max32664c/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX32664C 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_MAX32664C`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_MAX32664C)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MAX32664C_SAMPLE_BUFFER_SIZE"></a>

## 159.3 `CONFIG_MAX32664C_SAMPLE_BUFFER_SIZE`

**提示（Prompt）**：I2C 读取线程的采样缓冲区（Sample Buffer）长度

**说明（Help）**

一次从传感器集线器（Sensor Hub）读取的采样数量。最大值为 64；如果需要减少内存占用，可以设置更小的值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MAX32664C_USE_STATIC_MEMORY && CONFIG_SENSOR_MAX32664C && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`drivers/sensor/adi/max32664c/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max32664c/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX32664C 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_MAX32664C_USE_STATIC_MEMORY`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MAX32664C_USE_STATIC_MEMORY)、[`CONFIG_SENSOR_MAX32664C`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_MAX32664C)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MAX32664C_THREAD_STACK_SIZE"></a>

## 159.4 `CONFIG_MAX32664C_THREAD_STACK_SIZE`

**提示（Prompt）**：MAX32664C 采样线程栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR_MAX32664C && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/sensor/adi/max32664c/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max32664c/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX32664C 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_MAX32664C`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_MAX32664C)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MAX32664C_USE_EXTENDED_REPORTS"></a>

## 159.5 `CONFIG_MAX32664C_USE_EXTENDED_REPORTS`

**提示（Prompt）**：需要使用扩展报告（Extended Reports）代替默认报告时，启用此选项。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR_MAX32664C && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/adi/max32664c/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max32664c/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX32664C 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_MAX32664C`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_MAX32664C)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MAX32664C_USE_EXTERNAL_ACC"></a>

## 159.6 `CONFIG_MAX32664C_USE_EXTERNAL_ACC`

**提示（Prompt）**：需要使用外部加速度计（External Accelerometer）时，启用此选项。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR_MAX32664C && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/adi/max32664c/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max32664c/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX32664C 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_MAX32664C`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_MAX32664C)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MAX32664C_USE_FIRMWARE_LOADER"></a>

## 159.7 `CONFIG_MAX32664C_USE_FIRMWARE_LOADER`

**提示（Prompt）**：需要通过 I2C 固件加载器（Firmware Loader）为传感器集线器（Sensor Hub）烧写固件时，启用此选项。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR_MAX32664C && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/adi/max32664c/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max32664c/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX32664C 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_MAX32664C`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_MAX32664C)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MAX32664C_USE_INTERRUPT"></a>

## 159.8 `CONFIG_MAX32664C_USE_INTERRUPT`

**提示（Prompt）**：需要使用 MFIO 中断支持时，启用此选项。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && CONFIG_SENSOR_MAX32664C && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/adi/max32664c/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max32664c/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX32664C 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SENSOR_MAX32664C`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_MAX32664C)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MAX32664C_USE_STATIC_MEMORY"></a>

## 159.9 `CONFIG_MAX32664C_USE_STATIC_MEMORY`

**提示（Prompt）**：如果驱动应使用动态内存（Dynamic Memory），请禁用此选项。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR_MAX32664C && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/adi/max32664c/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max32664c/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MAX32664C 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_MAX32664C`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_MAX32664C)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MAX44009"></a>

## 159.10 `CONFIG_MAX44009`

**提示（Prompt）**：MAX44009 光照传感器（Light Sensor）

**说明（Help）**

启用 MAX44009 光照传感器（Light Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX44009_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/maxim/max44009/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max44009/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MAX6675"></a>

## 159.11 `CONFIG_MAX6675`

**提示（Prompt）**：MAX6675 K 型热电偶数字转换器（K-thermocouple to Digital Converter）

**说明（Help）**

启用带冷端补偿（Cold-Junction Compensation）的 MAX6675 K 型热电偶数字转换器（K-thermocouple to Digital Converter）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX6675_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/sensor/maxim/max6675/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/max6675/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_MB7040"></a>

## 159.12 `CONFIG_MB7040`

**提示（Prompt）**：MB7040 超声波测距传感器（Ultrasonic Distance Sensor）

**说明（Help）**

启用 MB7040 测距传感器（Distance Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXBOTIX_MB7040_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/mb7040/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/mb7040/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MB7040_DELAY_MS"></a>

## 159.13 `CONFIG_MB7040_DELAY_MS`

**提示（Prompt）**：等待距离测量的延迟，单位为毫秒

**说明（Help）**

采样获取（Sample Fetch）的超时时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MB7040 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/sensor/mb7040/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/mb7040/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MB7040 超声波测距传感器（Ultrasonic Distance Sensor）

**配置项引用（Symbol References）**：[`CONFIG_MB7040`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MB7040)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MC3419"></a>

## 159.14 `CONFIG_MC3419`

**提示（Prompt）**：MC3419 加速度计（Accelerometer）驱动

**说明（Help）**

启用 MC3419 加速度计（Accelerometer）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MEMSIC_MC3419_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
```

**定义位置（Location）**：[`drivers/sensor/memsic/mc3419/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/memsic/mc3419/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MC3419_THREAD_PRIORITY"></a>

## 159.15 `CONFIG_MC3419_THREAD_PRIORITY`

**提示（Prompt）**：专用线程优先级（Own Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MC3419_TRIGGER_OWN_THREAD && CONFIG_MC3419_TRIGGER && CONFIG_MC3419 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/memsic/mc3419/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/memsic/mc3419/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MC3419 加速度计（Accelerometer）驱动

**配置项引用（Symbol References）**：[`CONFIG_MC3419_TRIGGER_OWN_THREAD`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MC3419_TRIGGER_OWN_THREAD)、[`CONFIG_MC3419_TRIGGER`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MC3419_TRIGGER)、[`CONFIG_MC3419`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MC3419)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MC3419_THREAD_STACK_SIZE"></a>

## 159.16 `CONFIG_MC3419_THREAD_STACK_SIZE`

**提示（Prompt）**：专用线程栈大小（Own Thread Stack Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MC3419_TRIGGER_OWN_THREAD && CONFIG_MC3419_TRIGGER && CONFIG_MC3419 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/memsic/mc3419/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/memsic/mc3419/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MC3419 加速度计（Accelerometer）驱动

**配置项引用（Symbol References）**：[`CONFIG_MC3419_TRIGGER_OWN_THREAD`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MC3419_TRIGGER_OWN_THREAD)、[`CONFIG_MC3419_TRIGGER`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MC3419_TRIGGER)、[`CONFIG_MC3419`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MC3419)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MC3419_TRIGGER"></a>

## 159.17 `CONFIG_MC3419_TRIGGER`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_MC3419_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/memsic/mc3419/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/memsic/mc3419/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MC3419 加速度计（Accelerometer）驱动

**配置项引用（Symbol References）**：[`CONFIG_MC3419_TRIGGER_OWN_THREAD`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MC3419_TRIGGER_OWN_THREAD)。

<a id="CONFIG_MC3419_TRIGGER_MODE"></a>

## 159.18 `CONFIG_MC3419_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MC3419 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_MC3419_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_MC3419_TRIGGER_NONE
CONFIG_MC3419_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/memsic/mc3419/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/memsic/mc3419/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MC3419 加速度计（Accelerometer）驱动

**配置项引用（Symbol References）**：[`CONFIG_MC3419`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MC3419)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_MC3419_TRIGGER_NONE`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MC3419_TRIGGER_NONE)、[`CONFIG_MC3419_TRIGGER_OWN_THREAD`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MC3419_TRIGGER_OWN_THREAD)。

<a id="CONFIG_MC3419_TRIGGER_NONE"></a>

## 159.19 `CONFIG_MC3419_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MC3419_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/memsic/mc3419/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/memsic/mc3419/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MC3419 加速度计（Accelerometer）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_MC3419_TRIGGER_MODE`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MC3419_TRIGGER_MODE)。

<a id="CONFIG_MC3419_TRIGGER_OWN_THREAD"></a>

## 159.20 `CONFIG_MC3419_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**

启用后，在专用线程（Own Thread）中处理触发事件；默认使用全局线程模式（Global Thread Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MC3419_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MC3419_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/memsic/mc3419/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/memsic/mc3419/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MC3419 加速度计（Accelerometer）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_MC3419_TRIGGER_MODE`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MC3419_TRIGGER_MODE)、[`CONFIG_MC3419_TRIGGER`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MC3419_TRIGGER)。

<a id="CONFIG_MCP9600"></a>

## 159.21 `CONFIG_MCP9600`

**提示（Prompt）**：MCP9600 I2C 热电偶温度传感器（Thermocouple Temperature Sensor）

**说明（Help）**

启用 MCP9600 I2C 热电偶温度传感器（Thermocouple Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MCP9600_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/microchip/mcp9600/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/mcp9600/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MCP970X"></a>

## 159.22 `CONFIG_MCP970X`

**提示（Prompt）**：MCP9700/9700A 与 MCP9701/9701A 传感器

**说明（Help）**

启用低功耗线性有源热敏电阻集成电路（Low-Power Linear Active Thermistor IC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MCP970X_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/sensor/microchip/mcp970x/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/mcp970x/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_MCUX_LPCMP"></a>

## 159.23 `CONFIG_MCUX_LPCMP`

**提示（Prompt）**：NXP LPCMP 驱动［已弃用，DEPRECATED］

**说明（Help）**

启用 MCUX LPCMP 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPCMP_ENABLED && !CONFIG_COMPARATOR_NXP_LPCMP && CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/sensor/nxp/mcux_lpcmp/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/mcux_lpcmp/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR_NXP_LPCMP`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_NXP_LPCMP)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_MCUX_LPCMP_TRIGGER"></a>

## 159.24 `CONFIG_MCUX_LPCMP_TRIGGER`

**提示（Prompt）**：触发支持（Trigger Support）［已弃用，DEPRECATED］

**说明（Help）**

启用 NXP LPCMP 的触发支持（Trigger Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_LPCMP && CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/sensor/nxp/mcux_lpcmp/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/mcux_lpcmp/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → NXP LPCMP 驱动［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_MCUX_LPCMP`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MCUX_LPCMP)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_MHZ19B"></a>

## 159.25 `CONFIG_MHZ19B`

**提示（Prompt）**：Winsen 二氧化碳传感器（CO2 Sensor）

**说明（Help）**

启用 MHZ19B 二氧化碳传感器（CO2 Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WINSEN_MHZ19B_ENABLED && CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/mhz19b/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/mhz19b/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MLX90394"></a>

## 159.26 `CONFIG_MLX90394`

**提示（Prompt）**：MLX90394 磁力计（Magnetometer）

**说明（Help）**

启用 MLX90394 磁力计（Magnetometer）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MELEXIS_MLX90394_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/melexis/mlx90394/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/melexis/mlx90394/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MMC56X3"></a>

## 159.27 `CONFIG_MMC56X3`

**提示（Prompt）**：Memsic MMC56X3 磁力计（Magnetometer）驱动

**说明（Help）**

启用 MMC56X3 磁力计与温度传感器（Magnetometer and Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MEMSIC_MMC56X3_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
```

**定义位置（Location）**：[`drivers/sensor/memsic/mmc56x3/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/memsic/mmc56x3/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MPR"></a>

## 159.28 `CONFIG_MPR`

**提示（Prompt）**：MPR 压力传感器（Pressure Sensor）

**说明（Help）**

启用 MPR 压力传感器（Pressure Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HONEYWELL_MPR_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MPR_PRESSURE_RANGE_0001"></a>

## 159.29 `CONFIG_MPR_PRESSURE_RANGE_0001`

**提示（Prompt）**：0 至 1

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力范围（Pressure Range）

<a id="CONFIG_MPR_PRESSURE_RANGE_0015"></a>

## 159.30 `CONFIG_MPR_PRESSURE_RANGE_0015`

**提示（Prompt）**：0 至 15

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力范围（Pressure Range）

<a id="CONFIG_MPR_PRESSURE_RANGE_0025"></a>

## 159.31 `CONFIG_MPR_PRESSURE_RANGE_0025`

**提示（Prompt）**：0 至 25

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力范围（Pressure Range）

<a id="CONFIG_MPR_PRESSURE_RANGE_0030"></a>

## 159.32 `CONFIG_MPR_PRESSURE_RANGE_0030`

**提示（Prompt）**：0 至 30

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力范围（Pressure Range）

<a id="CONFIG_MPR_PRESSURE_RANGE_0060"></a>

## 159.33 `CONFIG_MPR_PRESSURE_RANGE_0060`

**提示（Prompt）**：0 至 60

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力范围（Pressure Range）

<a id="CONFIG_MPR_PRESSURE_RANGE_0100"></a>

## 159.34 `CONFIG_MPR_PRESSURE_RANGE_0100`

**提示（Prompt）**：0 至 100

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力范围（Pressure Range）

<a id="CONFIG_MPR_PRESSURE_RANGE_0160"></a>

## 159.35 `CONFIG_MPR_PRESSURE_RANGE_0160`

**提示（Prompt）**：0 至 160

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力范围（Pressure Range）

<a id="CONFIG_MPR_PRESSURE_RANGE_01_6"></a>

## 159.36 `CONFIG_MPR_PRESSURE_RANGE_01_6`

**提示（Prompt）**：0 至 1.6

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力范围（Pressure Range）

<a id="CONFIG_MPR_PRESSURE_RANGE_0250"></a>

## 159.37 `CONFIG_MPR_PRESSURE_RANGE_0250`

**提示（Prompt）**：0 至 250

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力范围（Pressure Range）

<a id="CONFIG_MPR_PRESSURE_RANGE_02_5"></a>

## 159.38 `CONFIG_MPR_PRESSURE_RANGE_02_5`

**提示（Prompt）**：0 至 2.5

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力范围（Pressure Range）

<a id="CONFIG_MPR_PRESSURE_RANGE_0400"></a>

## 159.39 `CONFIG_MPR_PRESSURE_RANGE_0400`

**提示（Prompt）**：0 至 400

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力范围（Pressure Range）

<a id="CONFIG_MPR_PRESSURE_RANGE_0600"></a>

## 159.40 `CONFIG_MPR_PRESSURE_RANGE_0600`

**提示（Prompt）**：0 至 600

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力范围（Pressure Range）

<a id="CONFIG_MPR_PRESSURE_UNIT_B"></a>

## 159.41 `CONFIG_MPR_PRESSURE_UNIT_B`

**提示（Prompt）**：巴（bar）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力单位（Pressure Unit）

<a id="CONFIG_MPR_PRESSURE_UNIT_K"></a>

## 159.42 `CONFIG_MPR_PRESSURE_UNIT_K`

**提示（Prompt）**：千帕（kPa）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力单位（Pressure Unit）

<a id="CONFIG_MPR_PRESSURE_UNIT_M"></a>

## 159.43 `CONFIG_MPR_PRESSURE_UNIT_M`

**提示（Prompt）**：毫巴（mbar）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力单位（Pressure Unit）

<a id="CONFIG_MPR_PRESSURE_UNIT_P"></a>

## 159.44 `CONFIG_MPR_PRESSURE_UNIT_P`

**提示（Prompt）**：磅力／平方英寸（psi）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 压力单位（Pressure Unit）

<a id="CONFIG_MPR_TRANSFER_FUNCTION_A"></a>

## 159.45 `CONFIG_MPR_TRANSFER_FUNCTION_A`

**提示（Prompt）**：A

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 传递函数（Transfer Function）

<a id="CONFIG_MPR_TRANSFER_FUNCTION_B"></a>

## 159.46 `CONFIG_MPR_TRANSFER_FUNCTION_B`

**提示（Prompt）**：B

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 传递函数（Transfer Function）

<a id="CONFIG_MPR_TRANSFER_FUNCTION_C"></a>

## 159.47 `CONFIG_MPR_TRANSFER_FUNCTION_C`

**提示（Prompt）**：C

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/honeywell/mpr/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/mpr/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPR 压力传感器（Pressure Sensor） → MPR 传递函数（Transfer Function）

<a id="CONFIG_MPU6050"></a>

## 159.48 `CONFIG_MPU6050`

**提示（Prompt）**：MPU6050 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**说明（Help）**

启用基于 I2C 的 MPU6050 六轴运动跟踪器件（Six-axis Motion Tracking Device）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INVENSENSE_MPU6050_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/tdk/mpu6050/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/mpu6050/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MPU6050_THREAD_PRIORITY"></a>

## 159.49 `CONFIG_MPU6050_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPU6050_TRIGGER_OWN_THREAD && CONFIG_MPU6050 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/tdk/mpu6050/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/mpu6050/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPU6050 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_MPU6050_TRIGGER_OWN_THREAD`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MPU6050_TRIGGER_OWN_THREAD)、[`CONFIG_MPU6050`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MPU6050)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MPU6050_THREAD_STACK_SIZE"></a>

## 159.50 `CONFIG_MPU6050_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPU6050_TRIGGER_OWN_THREAD && CONFIG_MPU6050 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/tdk/mpu6050/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/mpu6050/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPU6050 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_MPU6050_TRIGGER_OWN_THREAD`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MPU6050_TRIGGER_OWN_THREAD)、[`CONFIG_MPU6050`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MPU6050)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MPU6050_TRIGGER_GLOBAL_THREAD"></a>

## 159.51 `CONFIG_MPU6050_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_MPU6050_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/tdk/mpu6050/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/mpu6050/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPU6050 六轴运动跟踪器件（Six-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_MPU6050_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPU6050_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MPU6050_TRIGGER`。

<a id="CONFIG_MPU6050_TRIGGER_NONE"></a>

## 159.52 `CONFIG_MPU6050_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/tdk/mpu6050/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/mpu6050/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPU6050 六轴运动跟踪器件（Six-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

<a id="CONFIG_MPU6050_TRIGGER_OWN_THREAD"></a>

## 159.53 `CONFIG_MPU6050_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_MPU6050_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/tdk/mpu6050/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/mpu6050/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPU6050 六轴运动跟踪器件（Six-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_MPU6050_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPU6050_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MPU6050_TRIGGER`。

<a id="CONFIG_MPU9250"></a>

## 159.54 `CONFIG_MPU9250`

**提示（Prompt）**：MPU9250 九轴运动跟踪器件（Nine-Axis Motion Tracking Device）

**说明（Help）**

启用基于 I2C 的 MPU9250 九轴运动跟踪器件（Nine-axis Motion Tracking Device）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INVENSENSE_MPU9250_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/tdk/mpu9250/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/mpu9250/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MPU9250_MAGN_EN"></a>

## 159.55 `CONFIG_MPU9250_MAGN_EN`

**提示（Prompt）**：启用磁力计（Magnetometer）

**说明（Help）**

启用内置 AK8963 磁力计（Magnetometer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MPU9250 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/tdk/mpu9250/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/mpu9250/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPU9250 九轴运动跟踪器件（Nine-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_MPU9250`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MPU9250)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MPU9250_THREAD_PRIORITY"></a>

## 159.56 `CONFIG_MPU9250_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPU9250_TRIGGER_OWN_THREAD && CONFIG_MPU9250 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/tdk/mpu9250/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/mpu9250/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPU9250 九轴运动跟踪器件（Nine-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_MPU9250_TRIGGER_OWN_THREAD`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MPU9250_TRIGGER_OWN_THREAD)、[`CONFIG_MPU9250`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MPU9250)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MPU9250_THREAD_STACK_SIZE"></a>

## 159.57 `CONFIG_MPU9250_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MPU9250_TRIGGER_OWN_THREAD && CONFIG_MPU9250 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/tdk/mpu9250/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/mpu9250/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPU9250 九轴运动跟踪器件（Nine-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_MPU9250_TRIGGER_OWN_THREAD`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MPU9250_TRIGGER_OWN_THREAD)、[`CONFIG_MPU9250`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MPU9250)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MPU9250_TRIGGER_GLOBAL_THREAD"></a>

## 159.58 `CONFIG_MPU9250_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_MPU9250_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/tdk/mpu9250/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/mpu9250/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPU9250 九轴运动跟踪器件（Nine-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_MPU9250_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPU9250_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MPU9250_TRIGGER`。

<a id="CONFIG_MPU9250_TRIGGER_NONE"></a>

## 159.59 `CONFIG_MPU9250_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/tdk/mpu9250/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/mpu9250/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPU9250 九轴运动跟踪器件（Nine-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

<a id="CONFIG_MPU9250_TRIGGER_OWN_THREAD"></a>

## 159.60 `CONFIG_MPU9250_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_MPU9250_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/tdk/mpu9250/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/mpu9250/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MPU9250 九轴运动跟踪器件（Nine-Axis Motion Tracking Device） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_MPU9250_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPU9250_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MPU9250_TRIGGER`。

<a id="CONFIG_MS5607"></a>

## 159.61 `CONFIG_MS5607`

**提示（Prompt）**：MS5607 压力与温度传感器（Pressure and Temperature Sensor）

**说明（Help）**

启用 MS5607 压力与温度传感器（Pressure and Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MEAS_MS5607_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
```

**定义位置（Location）**：[`drivers/sensor/meas/ms5607/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/meas/ms5607/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_MS5607_PRES_OVER_1024X"></a>

## 159.62 `CONFIG_MS5607_PRES_OVER_1024X`

**提示（Prompt）**：1024 倍（x1024）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/meas/ms5607/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/meas/ms5607/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MS5607 压力与温度传感器（Pressure and Temperature Sensor） → 压力过采样（Pressure Oversampling）。

<a id="CONFIG_MS5607_PRES_OVER_2048X"></a>

## 159.63 `CONFIG_MS5607_PRES_OVER_2048X`

**提示（Prompt）**：2048 倍（x2048）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/meas/ms5607/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/meas/ms5607/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MS5607 压力与温度传感器（Pressure and Temperature Sensor） → 压力过采样（Pressure Oversampling）。

<a id="CONFIG_MS5607_PRES_OVER_256X"></a>

## 159.64 `CONFIG_MS5607_PRES_OVER_256X`

**提示（Prompt）**：256 倍（x256）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/meas/ms5607/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/meas/ms5607/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MS5607 压力与温度传感器（Pressure and Temperature Sensor） → 压力过采样（Pressure Oversampling）。

<a id="CONFIG_MS5607_PRES_OVER_4096X"></a>

## 159.65 `CONFIG_MS5607_PRES_OVER_4096X`

**提示（Prompt）**：4096 倍（x4096）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/meas/ms5607/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/meas/ms5607/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MS5607 压力与温度传感器（Pressure and Temperature Sensor） → 压力过采样（Pressure Oversampling）。

<a id="CONFIG_MS5607_PRES_OVER_512X"></a>

## 159.66 `CONFIG_MS5607_PRES_OVER_512X`

**提示（Prompt）**：512 倍（x512）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/meas/ms5607/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/meas/ms5607/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MS5607 压力与温度传感器（Pressure and Temperature Sensor） → 压力过采样（Pressure Oversampling）。

<a id="CONFIG_MS5607_TEMP_OVER_1024X"></a>

## 159.67 `CONFIG_MS5607_TEMP_OVER_1024X`

**提示（Prompt）**：1024 倍（x1024）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/meas/ms5607/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/meas/ms5607/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MS5607 压力与温度传感器（Pressure and Temperature Sensor） → 温度过采样（Temperature Oversampling）。

<a id="CONFIG_MS5607_TEMP_OVER_2048X"></a>

## 159.68 `CONFIG_MS5607_TEMP_OVER_2048X`

**提示（Prompt）**：2048 倍（x2048）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/meas/ms5607/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/meas/ms5607/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MS5607 压力与温度传感器（Pressure and Temperature Sensor） → 温度过采样（Temperature Oversampling）。

<a id="CONFIG_MS5607_TEMP_OVER_256X"></a>

## 159.69 `CONFIG_MS5607_TEMP_OVER_256X`

**提示（Prompt）**：256 倍（x256）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/meas/ms5607/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/meas/ms5607/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MS5607 压力与温度传感器（Pressure and Temperature Sensor） → 温度过采样（Temperature Oversampling）。

<a id="CONFIG_MS5607_TEMP_OVER_4096X"></a>

## 159.70 `CONFIG_MS5607_TEMP_OVER_4096X`

**提示（Prompt）**：4096 倍（x4096）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/meas/ms5607/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/meas/ms5607/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MS5607 压力与温度传感器（Pressure and Temperature Sensor） → 温度过采样（Temperature Oversampling）。

<a id="CONFIG_MS5607_TEMP_OVER_512X"></a>

## 159.71 `CONFIG_MS5607_TEMP_OVER_512X`

**提示（Prompt）**：512 倍（x512）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/meas/ms5607/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/meas/ms5607/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MS5607 压力与温度传感器（Pressure and Temperature Sensor） → 温度过采样（Temperature Oversampling）。

<a id="CONFIG_MS5637"></a>

## 159.72 `CONFIG_MS5637`

**提示（Prompt）**：MS5637 压力与温度传感器（Pressure and Temperature Sensor）

**说明（Help）**

启用通过 I2C 通信的 TE Connectivity MS5637 数字压力与温度传感器（Digital Pressure and Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MEAS_MS5637_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_I2C_RTIO if CONFIG_SENSOR_ASYNC_API
CONFIG_RTIO_OP_DELAY if CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/meas/ms5637/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/meas/ms5637/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_RTIO_OP_DELAY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_OP_DELAY)。

<a id="CONFIG_MS5837"></a>

## 159.73 `CONFIG_MS5837`

**提示（Prompt）**：MS5837 压力与温度传感器（Pressure and Temperature Sensor）

**说明（Help）**

启用 MS5837 压力与温度传感器（Pressure and Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_MEAS_MS5837_02BA_ENABLED || DT_HAS_MEAS_MS5837_30BA_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/meas/ms5837/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/meas/ms5837/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_MTCH9010"></a>

## 159.74 `CONFIG_MTCH9010`

**提示（Prompt）**：MTCH9010

**说明（Help）**

配置 MTCH9010 驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_MTCH9010_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/microchip/mtch9010/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/mtch9010/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MTCH9010_HEARTBEAT_MONITORING_ENABLE"></a>

## 159.75 `CONFIG_MTCH9010_HEARTBEAT_MONITORING_ENABLE`

**提示（Prompt）**：心跳监测（Heartbeat Monitoring）

**说明（Help）**

配置对心跳输出（Heartbeat Output）的监测。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MTCH9010 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/microchip/mtch9010/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/mtch9010/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MTCH9010

**配置项引用（Symbol References）**：[`CONFIG_MTCH9010`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MTCH9010)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MTCH9010_LOCK_ON_STARTUP"></a>

## 159.76 `CONFIG_MTCH9010_LOCK_ON_STARTUP`

**提示（Prompt）**：启动时保存 MTCH9010 设置

**说明（Help）**

启用此选项后，初始化完成时将置位 SYS_LK。如果下次上电复位（Power-on Reset，POR）时 SYS_LK 处于有效状态，传感器将使用这些参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MTCH9010 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/sensor/microchip/mtch9010/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/mtch9010/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MTCH9010

**配置项引用（Symbol References）**：[`CONFIG_MTCH9010`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MTCH9010)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MTCH9010_OVERRIDE_DELAY_ENABLE"></a>

## 159.77 `CONFIG_MTCH9010_OVERRIDE_DELAY_ENABLE`

**提示（Prompt）**：未采用按请求唤醒（Wake on Request）时覆盖延迟设置

**说明（Help）**

如果 MTCH9010 定义了睡眠周期（Sleep Period），唤醒引脚将无法唤醒设备。启用此选项后，API 在获取采样期间将允许长度为 `<sleep period + timeout>`（睡眠周期＋超时时间）的延迟。否则，API 使用正常超时时间，操作很可能失败。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MTCH9010 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/microchip/mtch9010/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/mtch9010/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MTCH9010

**配置项引用（Symbol References）**：[`CONFIG_MTCH9010`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MTCH9010)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MTCH9010_REFERENCE_AVERAGING_COUNT"></a>

## 159.78 `CONFIG_MTCH9010_REFERENCE_AVERAGING_COUNT`

**提示（Prompt）**：参考值平均采样数（Reference Averaging Count）

**说明（Help）**

如果 MTCH9010 使用当前测量值作为参考值，此选项指定用于求平均的采样数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MTCH9010 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`drivers/sensor/microchip/mtch9010/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/mtch9010/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MTCH9010

**配置项引用（Symbol References）**：[`CONFIG_MTCH9010`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MTCH9010)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MTCH9010_RESET_ON_STARTUP"></a>

## 159.79 `CONFIG_MTCH9010_RESET_ON_STARTUP`

**提示（Prompt）**：启动时复位 MTCH9010

**说明（Help）**

在驱动配置 MTCH9010 之前将其复位。如果禁用此选项且 MTCH9010 已经配置过，配置操作将失败。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MTCH9010 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/microchip/mtch9010/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/mtch9010/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MTCH9010

**配置项引用（Symbol References）**：[`CONFIG_MTCH9010`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MTCH9010)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_MTCH9010_SAMPLE_DELAY_TIMEOUT_MS"></a>

## 159.80 `CONFIG_MTCH9010_SAMPLE_DELAY_TIMEOUT_MS`

**提示（Prompt）**：取得一个采样的最长等待时间（ms）

**说明（Help）**

设置请求采样时等待 MTCH9010 响应的最长时间，单位为毫秒。导电模式（Conductive Mode）比电容模式（Capacitive Mode）快得多。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MTCH9010 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/sensor/microchip/mtch9010/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/mtch9010/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MTCH9010

**配置项引用（Symbol References）**：[`CONFIG_MTCH9010`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MTCH9010)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_NATIVE_LINUX_TEMP"></a>

## 159.81 `CONFIG_NATIVE_LINUX_TEMP`

**提示（Prompt）**：原生 Linux 主机温度传感器（Native Linux Host Temperature Sensor）

**说明（Help）**

启用由 Linux sysfs 温度文件提供数据的 `native_sim` 温度传感器。设备树（Devicetree）节点通过 `path` 属性指定文件位置，例如 `/sys/class/thermal/thermal_zone0/temp`。

译注：此处路径为原文中的 Linux 系统接口示例，不是本仓库的安装位置或本机仓库绝对路径。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_NATIVE_LINUX_TEMP_ENABLED && CONFIG_ARCH_POSIX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/linux_temp/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/linux_temp/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_NCT75"></a>

## 159.82 `CONFIG_NCT75`

**提示（Prompt）**：NCT75 温度传感器（Temperature Sensor）

**说明（Help）**

启用 NCT75 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ONNN_NCT75_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/nct75/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nct75/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_NPM10XX_ADC"></a>

## 159.83 `CONFIG_NPM10XX_ADC`

**提示（Prompt）**：nPM10xx 模数转换器（ADC）驱动

**说明（Help）**

启用 Nordic nPM10xx 模数转换器（ADC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM10XX_ADC_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/nordic/npm10xx_adc/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nordic/npm10xx_adc/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_NPM13XX_CHARGER"></a>

## 159.84 `CONFIG_NPM13XX_CHARGER`

**提示（Prompt）**：nPM13xx 充电器（Charger）

**说明（Help）**

启用 nPM13xx 充电器（Charger）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NORDIC_NPM1300_CHARGER_ENABLED || DT_HAS_NORDIC_NPM1304_CHARGER_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_MFD
CONFIG_REQUIRES_FULL_LIBC
```

**定义位置（Location）**：[`drivers/sensor/nordic/npm13xx_charger/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nordic/npm13xx_charger/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_REQUIRES_FULL_LIBC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REQUIRES_FULL_LIBC)。

<a id="CONFIG_NPM2100_VBAT"></a>

## 159.85 `CONFIG_NPM2100_VBAT`

**提示（Prompt）**：NPM2100 电池电压（Battery Voltage）

**说明（Help）**

启用 NPM2100 电池电压（Battery Voltage）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM2100_VBAT_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/sensor/nordic/npm2100_vbat/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nordic/npm2100_vbat/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_NRF_VBAT"></a>

## 159.86 `CONFIG_NRF_VBAT`

**提示（Prompt）**：nRF 电池电压传感器（通过 Zephyr ADC 使用 SAADC）

**说明（Help）**

启用 Nordic nRF VBAT 电池电压传感器驱动。设备树（Devicetree）节点必须通过 `io-channels` 指定一个 SAADC 通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_VBAT_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/sensor/nordic/vbat/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nordic/vbat/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_NTC_THERMISTOR"></a>

## 159.87 `CONFIG_NTC_THERMISTOR`

**提示（Prompt）**：负温度系数热敏电阻（NTC Thermistor）

**说明（Help）**

启用 Zephyr 负温度系数热敏电阻（NTC Thermistor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NTC_THERMISTOR_GENERIC_ENABLED || DT_HAS_EPCOS_B57861S0103A039_ENABLED || DT_HAS_MURATA_NCP15WB473_ENABLED || DT_HAS_TDK_NTCGXX3JX103X_ENABLED || DT_HAS_MURATA_NCP15XH103_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/sensor/ntc_thermistor/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ntc_thermistor/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_NXP_PMC_TMPSNS"></a>

## 159.88 `CONFIG_NXP_PMC_TMPSNS`

**提示（Prompt）**：NXP PMC 温度传感器（TMPSNS）

**说明（Help）**

启用 NXP PMC 温度传感器驱动，用于取得芯片裸片的工作温度（On-die Operational Temperature）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PMC_TMPSNS_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FPU if CONFIG_CPU_HAS_FPU
CONFIG_NVMEM if n
```

**弱选择（Implies）**

```text
CONFIG_OTP
```

**定义位置（Location）**：[`drivers/sensor/nxp/nxp_pmc_tmpsns/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/nxp_pmc_tmpsns/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)、[`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)、[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)。

<a id="CONFIG_NXP_PMC_TMPSNS_USE_FLOAT_CALC"></a>

## 159.89 `CONFIG_NXP_PMC_TMPSNS_USE_FLOAT_CALC`

**提示（Prompt）**：使用浮点数（Float）和浮点单元（FPU）

**说明（Help）**

启用时，驱动执行更多浮点计算。如果片上系统（SoC）具有浮点单元（FPU），建议选择此选项。测试表明，启用此选项可缩短代码执行时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_PMC_TMPSNS && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/nxp/nxp_pmc_tmpsns/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/nxp_pmc_tmpsns/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → NXP PMC 温度传感器（TMPSNS）

**配置项引用（Symbol References）**：[`CONFIG_NXP_PMC_TMPSNS`](P159_drivers_sensor_配置项参考_11.md#CONFIG_NXP_PMC_TMPSNS)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_NXP_TEMPMON"></a>

## 159.90 `CONFIG_NXP_TEMPMON`

**提示（Prompt）**：NXP 温度监测器（Temperature Monitor，TEMPMON）

**说明（Help）**

启用 NXP 温度监测器（TEMPMON）驱动，用于取得芯片裸片的工作温度（On-die Operational Temperature）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_TEMPMON_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/nxp/nxp_tempmon/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/nxp_tempmon/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_NXP_TEMPSENSE"></a>

## 159.91 `CONFIG_NXP_TEMPSENSE`

**提示（Prompt）**：NXP 温度传感器（Temperature Sensor，TEMPSENSE）

**说明（Help）**

启用 NXP 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_TEMPSENSE_ENABLED && CONFIG_ADC && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/nxp/nxp_tempsense/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/nxp_tempsense/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_NXP_TMPSNS"></a>

## 159.92 `CONFIG_NXP_TMPSNS`

**提示（Prompt）**：NXP TMPSNS 传感器（Sensor）

**说明（Help）**

启用 NXP TMPSNS 传感器的温度测量功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_TMPSNS_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FPU
```

**定义位置（Location）**：[`drivers/sensor/nxp/nxp_tmpsns/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/nxp_tmpsns/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)。

<a id="CONFIG_OPT300X"></a>

## 159.93 `CONFIG_OPT300X`

**提示（Prompt）**：OPT300X 光照传感器（Light Sensor）

**说明（Help）**

启用 OPT300X 光照传感器（Light Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_OPT3001_ENABLED || DT_HAS_TI_OPT3004_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/opt300x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/opt300x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_OPT300X_THREAD_PRIORITY"></a>

## 159.94 `CONFIG_OPT300X_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPT300X_TRIGGER_OWN_THREAD && CONFIG_OPT300X_TRIGGER && CONFIG_OPT300X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → OPT300X 光照传感器（Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_OPT300X_TRIGGER_OWN_THREAD`](P159_drivers_sensor_配置项参考_11.md#CONFIG_OPT300X_TRIGGER_OWN_THREAD)、[`CONFIG_OPT300X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPT300X_TRIGGER)、[`CONFIG_OPT300X`](P159_drivers_sensor_配置项参考_11.md#CONFIG_OPT300X)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPT300X_TRIGGER`。

<a id="CONFIG_OPT300X_THREAD_STACK_SIZE"></a>

## 159.95 `CONFIG_OPT300X_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPT300X_TRIGGER_OWN_THREAD && CONFIG_OPT300X_TRIGGER && CONFIG_OPT300X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → OPT300X 光照传感器（Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_OPT300X_TRIGGER_OWN_THREAD`](P159_drivers_sensor_配置项参考_11.md#CONFIG_OPT300X_TRIGGER_OWN_THREAD)、[`CONFIG_OPT300X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPT300X_TRIGGER)、[`CONFIG_OPT300X`](P159_drivers_sensor_配置项参考_11.md#CONFIG_OPT300X)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPT300X_TRIGGER`。

<a id="CONFIG_OPT300X_TRIGGER_GLOBAL_THREAD"></a>

## 159.96 `CONFIG_OPT300X_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_OPT300X_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_OPT300X_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → OPT300X 光照传感器（Light Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_OPT300X_TRIGGER_MODE`](P159_drivers_sensor_配置项参考_11.md#CONFIG_OPT300X_TRIGGER_MODE)、[`CONFIG_OPT300X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPT300X_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPT300X_TRIGGER`。

<a id="CONFIG_OPT300X_TRIGGER_MODE"></a>

## 159.97 `CONFIG_OPT300X_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定传感器模块使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPT300X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_OPT300X_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_OPT300X_TRIGGER_NONE
CONFIG_OPT300X_TRIGGER_GLOBAL_THREAD
CONFIG_OPT300X_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → OPT300X 光照传感器（Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_OPT300X`](P159_drivers_sensor_配置项参考_11.md#CONFIG_OPT300X)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_OPT300X_TRIGGER_NONE`](P159_drivers_sensor_配置项参考_11.md#CONFIG_OPT300X_TRIGGER_NONE)、[`CONFIG_OPT300X_TRIGGER_GLOBAL_THREAD`](P159_drivers_sensor_配置项参考_11.md#CONFIG_OPT300X_TRIGGER_GLOBAL_THREAD)、[`CONFIG_OPT300X_TRIGGER_OWN_THREAD`](P159_drivers_sensor_配置项参考_11.md#CONFIG_OPT300X_TRIGGER_OWN_THREAD)。

<a id="CONFIG_OPT300X_TRIGGER_NONE"></a>

## 159.98 `CONFIG_OPT300X_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPT300X_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → OPT300X 光照传感器（Light Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_OPT300X_TRIGGER_MODE`](P159_drivers_sensor_配置项参考_11.md#CONFIG_OPT300X_TRIGGER_MODE)。

<a id="CONFIG_OPT300X_TRIGGER_OWN_THREAD"></a>

## 159.99 `CONFIG_OPT300X_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_OPT300X_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_OPT300X_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → OPT300X 光照传感器（Light Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_OPT300X_TRIGGER_MODE`](P159_drivers_sensor_配置项参考_11.md#CONFIG_OPT300X_TRIGGER_MODE)、[`CONFIG_OPT300X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPT300X_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPT300X_TRIGGER`。

<a id="CONFIG_P3T1755"></a>

## 159.100 `CONFIG_P3T1755`

**提示（Prompt）**：P3T1755 数字温度传感器（Digital Temperature Sensor）驱动

**说明（Help）**

启用 P3T1755 数字温度传感器（Digital Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_P3T1755_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_I3C if n
```

**定义位置（Location）**：[`drivers/sensor/nxp/p3t1755/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/p3t1755/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)。

<!-- kconfig-navigation -->

[上一章](P158_drivers_sensor_配置项参考_10.md) · [返回大纲](大纲.md) · [下一章](P160_drivers_sensor_配置项参考_12.md)
