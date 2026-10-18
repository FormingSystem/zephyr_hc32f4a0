---
id: learning.zephyr-docs.kconfig-reference.page-160
title: "`drivers/sensor`配置项参考（12/15）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第160章\_`drivers/sensor`配置项参考（12/15）

本章翻译官方 Kconfig 数据库中 `drivers/sensor` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PAA3905"></a>

## 160.1 `CONFIG_PAA3905`

**提示（Prompt）**：PAA3905 光流传感器（Optical Flow Sensor）

**说明（Help）**

启用 PAA3905 光流传感器（Optical Flow Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PIXART_PAA3905_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_SPI_RTIO
CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/pixart/paa3905/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/pixart/paa3905/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_PAA3905_STREAM"></a>

## 160.2 `CONFIG_PAA3905_STREAM`

**提示（Prompt）**：流式模式（Streaming Mode）

**说明（Help）**

启用 PAA3905 传感器的流式模式（Streaming Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_RTIO_WORKQ
```

**定义位置（Location）**：[`drivers/sensor/pixart/paa3905/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/pixart/paa3905/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → PAA3905 光流传感器（Optical Flow Sensor）

**配置项引用（Symbol References）**：[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)。

<a id="CONFIG_PAC194X"></a>

## 160.3 `CONFIG_PAC194X`

**提示（Prompt）**：PAC194X/PAC195X 功率监测传感器（Power Monitor Sensor）

**说明（Help）**

启用 PAC194X/PAC195X 功率监测器（Power Monitor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_PAC194X_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/microchip/pac194x/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/microchip/pac194x/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_PAJ7620"></a>

## 160.4 `CONFIG_PAJ7620`

**提示（Prompt）**：PAJ7620 手势传感器（Gesture Sensor）驱动

**说明（Help）**

启用 PAJ7620 手势传感器（Gesture Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PIXART_PAJ7620_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/pixart/paj7620/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/pixart/paj7620/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_PAJ7620_THREAD_PRIORITY"></a>

## 160.5 `CONFIG_PAJ7620_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PAJ7620_TRIGGER_OWN_THREAD && CONFIG_PAJ7620_TRIGGER && CONFIG_PAJ7620 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → PAJ7620 手势传感器（Gesture Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_PAJ7620_TRIGGER_OWN_THREAD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAJ7620_TRIGGER_OWN_THREAD)、[`CONFIG_PAJ7620_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PAJ7620_TRIGGER)、[`CONFIG_PAJ7620`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAJ7620)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PAJ7620_TRIGGER`。

<a id="CONFIG_PAJ7620_THREAD_STACK_SIZE"></a>

## 160.6 `CONFIG_PAJ7620_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PAJ7620_TRIGGER_OWN_THREAD && CONFIG_PAJ7620_TRIGGER && CONFIG_PAJ7620 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → PAJ7620 手势传感器（Gesture Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_PAJ7620_TRIGGER_OWN_THREAD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAJ7620_TRIGGER_OWN_THREAD)、[`CONFIG_PAJ7620_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PAJ7620_TRIGGER)、[`CONFIG_PAJ7620`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAJ7620)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PAJ7620_TRIGGER`。

<a id="CONFIG_PAJ7620_TRIGGER_GLOBAL_THREAD"></a>

## 160.7 `CONFIG_PAJ7620_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_PAJ7620_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_PAJ7620_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → PAJ7620 手势传感器（Gesture Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PAJ7620_TRIGGER_MODE`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAJ7620_TRIGGER_MODE)、[`CONFIG_PAJ7620_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PAJ7620_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PAJ7620_TRIGGER`。

<a id="CONFIG_PAJ7620_TRIGGER_MODE"></a>

## 160.8 `CONFIG_PAJ7620_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定传感器模块使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PAJ7620 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_PAJ7620_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_PAJ7620_TRIGGER_NONE
CONFIG_PAJ7620_TRIGGER_GLOBAL_THREAD
CONFIG_PAJ7620_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → PAJ7620 手势传感器（Gesture Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_PAJ7620`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAJ7620)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_PAJ7620_TRIGGER_NONE`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAJ7620_TRIGGER_NONE)、[`CONFIG_PAJ7620_TRIGGER_GLOBAL_THREAD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAJ7620_TRIGGER_GLOBAL_THREAD)、[`CONFIG_PAJ7620_TRIGGER_OWN_THREAD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAJ7620_TRIGGER_OWN_THREAD)。

<a id="CONFIG_PAJ7620_TRIGGER_NONE"></a>

## 160.9 `CONFIG_PAJ7620_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PAJ7620_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → PAJ7620 手势传感器（Gesture Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_PAJ7620_TRIGGER_MODE`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAJ7620_TRIGGER_MODE)。

<a id="CONFIG_PAJ7620_TRIGGER_OWN_THREAD"></a>

## 160.10 `CONFIG_PAJ7620_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_PAJ7620_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_PAJ7620_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → PAJ7620 手势传感器（Gesture Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PAJ7620_TRIGGER_MODE`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAJ7620_TRIGGER_MODE)、[`CONFIG_PAJ7620_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PAJ7620_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PAJ7620_TRIGGER`。

<a id="CONFIG_PAT9136"></a>

## 160.11 `CONFIG_PAT9136`

**提示（Prompt）**：PAT9136 光流传感器（Optical Flow Sensor）

**说明（Help）**

启用 PAT9136 光流传感器（Optical Flow Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PIXART_PAT9136_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_SPI_RTIO
CONFIG_RTIO_WORKQ
CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/pixart/pat9136/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/pixart/pat9136/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_PAT9136_STREAM"></a>

## 160.12 `CONFIG_PAT9136_STREAM`

**提示（Prompt）**：流式模式（Streaming Mode）

**说明（Help）**

启用 PAT9136 传感器的流式模式（Streaming Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/sensor/pixart/pat9136/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/pixart/pat9136/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → PAT9136 光流传感器（Optical Flow Sensor）

<a id="CONFIG_PCNT_ESP32"></a>

## 160.13 `CONFIG_PCNT_ESP32`

**提示（Prompt）**：ESP32 脉冲计数器（Pulse Counter）驱动

**说明（Help）**

此选项为 ESP32 系列处理器启用脉冲计数器（PCNT）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_PCNT_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/espressif/pcnt_esp32/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/espressif/pcnt_esp32/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_PCNT_ESP32_TRIGGER"></a>

## 160.14 `CONFIG_PCNT_ESP32_TRIGGER`

**提示（Prompt）**：触发支持（Trigger Support）

**说明（Help）**

启用脉冲计数器（PCNT）的触发支持（Trigger Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PCNT_ESP32 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/espressif/pcnt_esp32/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/espressif/pcnt_esp32/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ESP32 脉冲计数器（Pulse Counter）驱动

**配置项引用（Symbol References）**：[`CONFIG_PCNT_ESP32`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PCNT_ESP32)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_PMS7003"></a>

## 160.15 `CONFIG_PMS7003`

**提示（Prompt）**：PMS7003 颗粒物传感器（Particulate Matter Sensor）

**说明（Help）**

启用 PMS7003 颗粒物传感器（Particulate Matter Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PLANTOWER_PMS7003_ENABLED && CONFIG_SERIAL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/plantower/pms7003/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/plantower/pms7003/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_PMSA003I"></a>

## 160.16 `CONFIG_PMSA003I`

**提示（Prompt）**：PMSA003I 颗粒物传感器（Particulate Matter Sensor）

**说明（Help）**

启用 PMSA003I 颗粒物传感器（Particulate Matter Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PLANTOWER_PMSA003I_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/plantower/pmsa003i/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/plantower/pmsa003i/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_PZEM004T"></a>

## 160.17 `CONFIG_PZEM004T`

**提示（Prompt）**：PZEM004T 多功能交流电表（Multifunction AC Meter）

**说明（Help）**

启用 Peacefair PZEM004T 多功能交流电表（Multifunction AC Meter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PEACEFAIR_PZEM004T_ENABLED && CONFIG_MODBUS && CONFIG_MODBUS_SERIAL && CONFIG_MODBUS_RAW_ADU && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MODBUS_NONCOMPLIANT_SERIAL_MODE
```

**定义位置（Location）**：[`drivers/sensor/pzem004t/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/pzem004t/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODBUS)、[`CONFIG_MODBUS_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODBUS_SERIAL)、[`CONFIG_MODBUS_RAW_ADU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODBUS_RAW_ADU)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_MODBUS_NONCOMPLIANT_SERIAL_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODBUS_NONCOMPLIANT_SERIAL_MODE)。

<a id="CONFIG_PZEM004T_ENABLE_RESET_ENERGY"></a>

## 160.18 `CONFIG_PZEM004T_ENABLE_RESET_ENERGY`

**提示（Prompt）**：包含电能值复位支持

**说明（Help）**

启用 PZEM004T 设备电能计数器（Energy Counter）的复位支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PZEM004T && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/pzem004t/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/pzem004t/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → PZEM004T 多功能交流电表（Multifunction AC Meter）

**配置项引用（Symbol References）**：[`CONFIG_PZEM004T`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PZEM004T)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_QDC_MCUX"></a>

## 160.19 `CONFIG_QDC_MCUX`

**提示（Prompt）**：NXP QDC MCUX 驱动

**说明（Help）**

启用 NXP MCUX QDC 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MCUX_QDC_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MUX
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/nxp/qdc_mcux/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/qdc_mcux/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_MUX`](P130_drivers_mux_配置项参考.md#CONFIG_MUX)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_QDEC_BEE"></a>

## 160.20 `CONFIG_QDEC_BEE`

**提示（Prompt）**：Realtek Bee 系列正交解码器（QDEC）驱动

**说明（Help）**

此选项为 Realtek Bee 片上系统（SoC）启用正交解码器（QDEC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_REALTEK_BEE_BASIC_QDEC_ENABLED || DT_HAS_REALTEK_BEE_AON_QDEC_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAL_REALTEK_BEE_QDEC if DT_HAS_REALTEK_BEE_BASIC_QDEC_ENABLED
CONFIG_HAL_REALTEK_BEE_AON_QDEC if DT_HAS_REALTEK_BEE_AON_QDEC_ENABLED
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/realtek/qdec_bee/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/realtek/qdec_bee/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_HAL_REALTEK_BEE_QDEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_QDEC)、[`CONFIG_HAL_REALTEK_BEE_AON_QDEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAL_REALTEK_BEE_AON_QDEC)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAL_REALTEK_BEE_QDEC`、`CONFIG_HAL_REALTEK_BEE_AON_QDEC`。

<a id="CONFIG_QDEC_MCUX"></a>

## 160.21 `CONFIG_QDEC_MCUX`

**提示（Prompt）**：NXP QDEC MCUX 驱动

**说明（Help）**

启用 NXP MCUX 正交编码器（Quadrature Encoder）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MCUX_QDEC_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MUX
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/nxp/qdec_mcux/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/qdec_mcux/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_MUX`](P130_drivers_mux_配置项参考.md#CONFIG_MUX)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_QDEC_NRFX"></a>

## 160.22 `CONFIG_QDEC_NRFX`

**提示（Prompt）**：Nordic QDEC nrfx 驱动

**说明（Help）**

为 nRF 微控制器（MCU）系列启用 nrfx 正交解码器（QDEC）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_QDEC_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_QDEC
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/nordic/qdec_nrfx/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nordic/qdec_nrfx/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_NRFX_QDEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_QDEC)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_QDEC_NXP_S32"></a>

## 160.23 `CONFIG_QDEC_NXP_S32`

**提示（Prompt）**：NXP S32 正交解码器（Quadrature Decoder）驱动

**说明（Help）**

启用 NXP S32 正交解码器（Quadrature Decoder）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_QDEC_S32_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NXP_S32_EMIOS
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/nxp/qdec_nxp_s32/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/qdec_nxp_s32/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_NXP_S32_EMIOS`](P123_drivers_misc_配置项参考.md#CONFIG_NXP_S32_EMIOS)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_QDEC_SAM"></a>

## 160.24 `CONFIG_QDEC_SAM`

**提示（Prompt）**：Atmel SAM QDEC 驱动

**说明（Help）**

Atmel SAM 微控制器（MCU）系列的正交解码器（Quadrature Decoder，TC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_TC_QDEC_ENABLED && CONFIG_SOC_FAMILY_ATMEL_SAM && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/qdec_sam/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/qdec_sam/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ATMEL_SAM`。

<a id="CONFIG_QDEC_STM32"></a>

## 160.25 `CONFIG_QDEC_STM32`

**提示（Prompt）**：STM32 QDEC 驱动

**说明（Help）**

STM32 系列正交解码器（Quadrature Decoder）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_QDEC_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/st/qdec_stm32/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/qdec_stm32/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_QDEC_TPM"></a>

## 160.26 `CONFIG_QDEC_TPM`

**提示（Prompt）**：NXP TPM 正交解码器（Quadrature Decoder）驱动

**说明（Help）**

启用 NXP TPM 正交解码器（Quadrature Decoder）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_TPM_QDEC_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/nxp/qdec_tpm/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/qdec_tpm/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_QMI8658A"></a>

## 160.27 `CONFIG_QMI8658A`

**提示（Prompt）**：QST QMI8658A 六轴惯性测量单元（6-axis IMU）

**说明（Help）**

启用 QST QMI8658A 六轴惯性测量单元（IMU）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_QST_QMI8658A_ENABLED && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/qst/qmi8658a/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/qst/qmi8658a/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_QMI8658A_THREAD_PRIORITY"></a>

## 160.28 `CONFIG_QMI8658A_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QMI8658A_TRIGGER_OWN_THREAD && CONFIG_QMI8658A_TRIGGER && CONFIG_QMI8658A && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → QST QMI8658A 六轴惯性测量单元（6-axis IMU）

**配置项引用（Symbol References）**：[`CONFIG_QMI8658A_TRIGGER_OWN_THREAD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_QMI8658A_TRIGGER_OWN_THREAD)、[`CONFIG_QMI8658A_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QMI8658A_TRIGGER)、[`CONFIG_QMI8658A`](P160_drivers_sensor_配置项参考_12.md#CONFIG_QMI8658A)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_QMI8658A_TRIGGER`。

<a id="CONFIG_QMI8658A_THREAD_STACK_SIZE"></a>

## 160.29 `CONFIG_QMI8658A_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QMI8658A_TRIGGER_OWN_THREAD && CONFIG_QMI8658A_TRIGGER && CONFIG_QMI8658A && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → QST QMI8658A 六轴惯性测量单元（6-axis IMU）

**配置项引用（Symbol References）**：[`CONFIG_QMI8658A_TRIGGER_OWN_THREAD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_QMI8658A_TRIGGER_OWN_THREAD)、[`CONFIG_QMI8658A_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QMI8658A_TRIGGER)、[`CONFIG_QMI8658A`](P160_drivers_sensor_配置项参考_12.md#CONFIG_QMI8658A)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_QMI8658A_TRIGGER`。

<a id="CONFIG_QMI8658A_TRIGGER_GLOBAL_THREAD"></a>

## 160.30 `CONFIG_QMI8658A_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_QMI8658A_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_QMI8658A_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → QST QMI8658A 六轴惯性测量单元（6-axis IMU） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_QMI8658A_TRIGGER_MODE`](P160_drivers_sensor_配置项参考_12.md#CONFIG_QMI8658A_TRIGGER_MODE)、[`CONFIG_QMI8658A_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QMI8658A_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_QMI8658A_TRIGGER`。

<a id="CONFIG_QMI8658A_TRIGGER_MODE"></a>

## 160.31 `CONFIG_QMI8658A_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定传感器模块使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_QMI8658A && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_QMI8658A_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_QMI8658A_TRIGGER_NONE
CONFIG_QMI8658A_TRIGGER_GLOBAL_THREAD
CONFIG_QMI8658A_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → QST QMI8658A 六轴惯性测量单元（6-axis IMU）

**配置项引用（Symbol References）**：[`CONFIG_QMI8658A`](P160_drivers_sensor_配置项参考_12.md#CONFIG_QMI8658A)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_QMI8658A_TRIGGER_NONE`](P160_drivers_sensor_配置项参考_12.md#CONFIG_QMI8658A_TRIGGER_NONE)、[`CONFIG_QMI8658A_TRIGGER_GLOBAL_THREAD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_QMI8658A_TRIGGER_GLOBAL_THREAD)、[`CONFIG_QMI8658A_TRIGGER_OWN_THREAD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_QMI8658A_TRIGGER_OWN_THREAD)。

<a id="CONFIG_QMI8658A_TRIGGER_NONE"></a>

## 160.32 `CONFIG_QMI8658A_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_QMI8658A_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → QST QMI8658A 六轴惯性测量单元（6-axis IMU） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_QMI8658A_TRIGGER_MODE`](P160_drivers_sensor_配置项参考_12.md#CONFIG_QMI8658A_TRIGGER_MODE)。

<a id="CONFIG_QMI8658A_TRIGGER_OWN_THREAD"></a>

## 160.33 `CONFIG_QMI8658A_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_QMI8658A_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_QMI8658A_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → QST QMI8658A 六轴惯性测量单元（6-axis IMU） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_QMI8658A_TRIGGER_MODE`](P160_drivers_sensor_配置项参考_12.md#CONFIG_QMI8658A_TRIGGER_MODE)、[`CONFIG_QMI8658A_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QMI8658A_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_QMI8658A_TRIGGER`。

<a id="CONFIG_R502A_DATA_PKT_SIZE"></a>

## 160.34 `CONFIG_R502A_DATA_PKT_SIZE`

**提示（Prompt）**：模板数据包大小（Template Data Packet Size）

**说明（Help）**

向传感器设备上传和下载时使用的模板数据包（Template Data Packet）大小。有效值为 32、64、128、256。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_GROW_R502A && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/sensor/grow_r502a/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/grow_r502a/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → GROW_R502A 指纹传感器（Fingerprint Sensor）

**配置项引用（Symbol References）**：[`CONFIG_GROW_R502A`](P153_drivers_sensor_配置项参考_5.md#CONFIG_GROW_R502A)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_RASPBERRYPI_BCM283X_VC_THERMAL"></a>

## 160.35 `CONFIG_RASPBERRYPI_BCM283X_VC_THERMAL`

**提示（Prompt）**：Raspberry Pi BCM283x VideoCore 片上系统温度传感器

**说明（Help）**

Raspberry Pi BCM283x 片上系统（SoC）的裸片温度传感器（Die-temperature Sensor）。通过 VideoCore 固件的 `GET_TEMPERATURE` 属性标签读取温度；这也是 `vcgencmd measure_temp` 的数据来源。温度通过 `SENSOR_CHAN_DIE_TEMP` 通道提供。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_BCM283X_VC_THERMAL_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RASPBERRYPI_FIRMWARE
```

**定义位置（Location）**：[`drivers/sensor/broadcom/bcm283x_vc_thermal/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/broadcom/bcm283x_vc_thermal/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_RASPBERRYPI_FIRMWARE`](P091_drivers_firmware_配置项参考.md#CONFIG_RASPBERRYPI_FIRMWARE)。

<a id="CONFIG_RM3100"></a>

## 160.36 `CONFIG_RM3100`

**提示（Prompt）**：RM3100 三轴磁力计（3-Axis Magnetometer）

**说明（Help）**

启用 PNI RM3100 高精度三轴磁力计（High-accuracy 3-axis Magnetometer）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PNI_RM3100_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI if n
CONFIG_SPI_RTIO if n
CONFIG_I2C if n
CONFIG_I2C_RTIO if n
CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/pni/rm3100/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/pni/rm3100/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_RM3100_STREAM"></a>

## 160.37 `CONFIG_RM3100_STREAM`

**提示（Prompt）**：RM3100 流式模式（Streaming Mode）

**说明（Help）**

启用 RM3100 传感器的流式模式（Streaming Mode），可按指定速率连续输出数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/sensor/pni/rm3100/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/pni/rm3100/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

<a id="CONFIG_RPI_PICO_TEMP"></a>

## 160.38 `CONFIG_RPI_PICO_TEMP`

**提示（Prompt）**：Raspberry Pi Pico CPU 温度传感器

**说明（Help）**

启用 Raspberry Pi Pico CPU 温度传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_TEMP_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/sensor/rpi_pico_temp/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/rpi_pico_temp/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_RV3032_TEMP"></a>

## 160.39 `CONFIG_RV3032_TEMP`

**提示（Prompt）**：RV3032 温度传感器（Temperature Sensor）

**说明（Help）**

启用 RV-3032-C7 实时时钟（RTC）上的温度传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCRYSTAL_RV3032_TEMP_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD_RV3032
```

**定义位置（Location）**：[`drivers/sensor/rv3032_temp/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/rv3032_temp/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_MFD_RV3032`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_RV3032)。

<a id="CONFIG_RV3032_TEMP_TRIGGER"></a>

## 160.40 `CONFIG_RV3032_TEMP_TRIGGER`

**提示（Prompt）**：触发支持（Trigger Support）

**说明（Help）**

启用 RV3032 TEMP 的触发支持（Trigger Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RV3032_TEMP && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/rv3032_temp/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/rv3032_temp/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → RV3032 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_RV3032_TEMP`](P160_drivers_sensor_配置项参考_12.md#CONFIG_RV3032_TEMP)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_S11059"></a>

## 160.41 `CONFIG_S11059`

**提示（Prompt）**：S11059 颜色传感器（Color Sensor）

**说明（Help）**

启用 S11059 颜色传感器（Color Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HAMAMATSU_S11059_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/s11059/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/s11059/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_S3KM1110"></a>

## 160.42 `CONFIG_S3KM1110`

**提示（Prompt）**：Iclegend S3KM1110 24 GHz 毫米波传感器（mmWave Sensor）

**说明（Help）**

启用 Iclegend S3KM1110 UART 雷达（Radar）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ICLEGEND_S3KM1110_ENABLED && CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/iclegend/s3km1110/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/iclegend/s3km1110/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_S3KM1110_UART_TIMEOUT_MS"></a>

## 160.43 `CONFIG_S3KM1110_UART_TIMEOUT_MS`

**提示（Prompt）**：UART 帧超时时间，单位为毫秒

**说明（Help）**

等待每个报告帧（Report Frame）时使用的超时时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_S3KM1110 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/sensor/iclegend/s3km1110/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/iclegend/s3km1110/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Iclegend S3KM1110 24 GHz 毫米波传感器（mmWave Sensor）

**配置项引用（Symbol References）**：[`CONFIG_S3KM1110`](P160_drivers_sensor_配置项参考_12.md#CONFIG_S3KM1110)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_S9706"></a>

## 160.44 `CONFIG_S9706`

**提示（Prompt）**：S9706 数字颜色传感器（Digital Color Sensor）

**说明（Help）**

启用 S9706 数字颜色传感器（Digital Color Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HAMAMATSU_S9706_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/sensor/s9706/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/s9706/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_S9706_DEFAULT_RANGE"></a>

## 160.45 `CONFIG_S9706_DEFAULT_RANGE`

**提示（Prompt）**：S9706：默认范围设置（Default Range Setting）

**说明（Help）**

选中时，驱动默认启用整个传感器；否则，仅使用中心部分。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_S9706 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/s9706/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/s9706/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → S9706 数字颜色传感器（Digital Color Sensor）

**配置项引用（Symbol References）**：[`CONFIG_S9706`](P160_drivers_sensor_配置项参考_12.md#CONFIG_S9706)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SBS_GAUGE"></a>

## 160.46 `CONFIG_SBS_GAUGE`

**提示（Prompt）**：智能电池电量计（Smart Battery Fuel Gauge）

**说明（Help）**

启用基于 I2C/SMBus 的智能电池电量计（Smart Battery Fuel Gauge）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SBS_SBS_GAUGE_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/sbs_gauge/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sbs_gauge/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_SCD4X"></a>

## 160.47 `CONFIG_SCD4X`

**提示（Prompt）**：SCD4x 二氧化碳传感器（Carbon Dioxide Sensor）

**说明（Help）**

启用 Sensirion SCD4x 二氧化碳传感器（Carbon Dioxide Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_SENSIRION_SCD41_ENABLED || DT_HAS_SENSIRION_SCD40_ENABLED) && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/sensirion/scd4x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/scd4x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_SENSOR"></a>

## 160.48 `CONFIG_SENSOR`

**提示（Prompt）**：传感器驱动（Sensor Drivers）

**说明（Help）**

在系统配置中包含传感器驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_NRF_802154_SL_OPENSOURCE
CONFIG_NRF_802154_SL_OPENSOURCE
CONFIG_BT_STM32WBA_USE_TEMP_BASED_CALIB
CONFIG_CLOCK_CONTROL_NRF_USES_TEMP_SENSOR
CONFIG_SENSING
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/rakwireless_rak19007/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rakwireless_rak19007/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/sensor/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_SL_OPENSOURCE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_802154_SL_OPENSOURCE)、[`CONFIG_BT_STM32WBA_USE_TEMP_BASED_CALIB`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA_USE_TEMP_BASED_CALIB)、[`CONFIG_CLOCK_CONTROL_NRF_USES_TEMP_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_USES_TEMP_SENSOR)、[`CONFIG_SENSING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_USES_TEMP_SENSOR`。

<a id="CONFIG_SENSOR_ASYNC_API"></a>

## 160.49 `CONFIG_SENSOR_ASYNC_API`

**提示（Prompt）**：异步传感器 API（Async Sensor API）

**说明（Help）**

通过实时输入输出（RTIO）子系统启用异步传感器 API（Asynchronous Sensor API）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_RTIO
CONFIG_RTIO_SYS_MEM_BLOCKS
CONFIG_RTIO_CONSUME_SEM
CONFIG_RTIO_WORKQ
```

**被选择（Selected by）**

```text
CONFIG_SENSOR_SHELL
CONFIG_MAX30009_STREAM
CONFIG_AFBR_S50
CONFIG_PAA3905
CONFIG_PAT9136
CONFIG_RM3100
CONFIG_ICM4268X_DECODER
CONFIG_ICM42X70
CONFIG_SENSING
```

**定义位置（Location）**：[`drivers/sensor/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO)、[`CONFIG_RTIO_SYS_MEM_BLOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_SYS_MEM_BLOCKS)、[`CONFIG_RTIO_CONSUME_SEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_CONSUME_SEM)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_SENSOR_SHELL`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_SHELL)、[`CONFIG_MAX30009_STREAM`](P158_drivers_sensor_配置项参考_10.md#CONFIG_MAX30009_STREAM)、[`CONFIG_AFBR_S50`](P150_drivers_sensor_配置项参考_2.md#CONFIG_AFBR_S50)、[`CONFIG_PAA3905`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAA3905)、[`CONFIG_PAT9136`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAT9136)、[`CONFIG_RM3100`](P160_drivers_sensor_配置项参考_12.md#CONFIG_RM3100)、[`CONFIG_ICM4268X_DECODER`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM4268X_DECODER)、[`CONFIG_ICM42X70`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42X70)、[`CONFIG_SENSING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSING)。

<a id="CONFIG_SENSOR_CLOCK"></a>

## 160.50 `CONFIG_SENSOR_CLOCK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

配置系统的传感器时钟源（Sensor Clock Source）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y if CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.sensor_clock:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.sensor_clock#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_SENSOR_CLOCK_COUNTER"></a>

## 160.51 `CONFIG_SENSOR_CLOCK_COUNTER`

**提示（Prompt）**：使用计数器设备／API（Counter Device/API）提供传感器时间

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.sensor_clock:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.sensor_clock#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 传感器时钟类型（Sensor Clock Type）

<a id="CONFIG_SENSOR_CLOCK_RTC"></a>

## 160.52 `CONFIG_SENSOR_CLOCK_RTC`

**提示（Prompt）**：使用实时时钟设备／API（RTC Device/API）提供传感器时间

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.sensor_clock:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.sensor_clock#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 传感器时钟类型（Sensor Clock Type）

<a id="CONFIG_SENSOR_CLOCK_SYSTEM"></a>

## 160.53 `CONFIG_SENSOR_CLOCK_SYSTEM`

**提示（Prompt）**：使用系统计数器（System Counter）提供传感器时间

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.sensor_clock:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.sensor_clock#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 传感器时钟类型（Sensor Clock Type）

<a id="CONFIG_SENSOR_DS3231"></a>

## 160.54 `CONFIG_SENSOR_DS3231`

**提示（Prompt）**：DS3231 传感器（Sensor）

**说明（Help）**

启用基于 I2C 的 DS3231 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_DS3231_MFD_ENABLED && DT_HAS_MAXIM_DS3231_SENSOR_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_MFD
CONFIG_RTIO_WORKQ if CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/maxim/ds3231/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/ds3231/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_SENSOR_DS3231_INIT_PRIORITY"></a>

## 160.55 `CONFIG_SENSOR_DS3231_INIT_PRIORITY`

**提示（Prompt）**：DS3231 传感器驱动初始化优先级（Init Priority）

**说明（Help）**

DS3231 传感器驱动的初始化优先级（Init Priority）。数值必须大于 `MFD_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR_DS3231 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
86
```

**定义位置（Location）**：[`drivers/sensor/maxim/ds3231/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/ds3231/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DS3231 传感器（Sensor）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_DS3231`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_DS3231)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SENSOR_GENERIC_EMUL"></a>

## 160.56 `CONFIG_SENSOR_GENERIC_EMUL`

**提示（Prompt）**：通用仿真传感器（Generic Emulated Sensor）

**说明（Help）**

由传感器仿真器后端 API（Sensor Emulator Backend API）控制的通用传感器设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_GENERIC_EMUL_SENSOR_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EMUL
```

**定义位置（Location）**：[`drivers/sensor/generic_emul/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/generic_emul/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)。

<a id="CONFIG_SENSOR_INFO"></a>

## 160.57 `CONFIG_SENSOR_INFO`

**提示（Prompt）**：传感器信息可迭代段（Sensor Info Iterable Section）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SENSOR_INIT_PRIORITY"></a>

## 160.58 `CONFIG_SENSOR_INIT_PRIORITY`

**提示（Prompt）**：传感器初始化优先级（Sensor Init Priority）

**说明（Help）**

传感器初始化优先级（Sensor Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/sensor/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SENSOR_MAX32664C"></a>

## 160.59 `CONFIG_SENSOR_MAX32664C`

**提示（Prompt）**：MAX32664C 驱动（Driver）

**说明（Help）**

启用 MAX32664C 生物识别传感器集线器（Biometric Sensor Hub）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX32664C_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/adi/max32664c/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max32664c/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_SENSOR_MCUX_ACMP"></a>

## 160.60 `CONFIG_SENSOR_MCUX_ACMP`

**提示（Prompt）**：NXP MCUX 模拟比较器（Analog Comparator，ACMP）

**说明（Help）**

启用 NXP MCUX 模拟比较器（Analog Comparator，ACMP）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_ACMP_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/nxp/mcux_acmp/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/mcux_acmp/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SENSOR_MCUX_ACMP_TRIGGER"></a>

## 160.61 `CONFIG_SENSOR_MCUX_ACMP_TRIGGER`

**提示（Prompt）**：触发支持（Trigger Support）

**说明（Help）**

启用 NXP MCUX 模拟比较器（Analog Comparator，ACMP）的触发支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR_MCUX_ACMP && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nxp/mcux_acmp/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/mcux_acmp/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → NXP MCUX 模拟比较器（Analog Comparator，ACMP）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_MCUX_ACMP`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_MCUX_ACMP)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SENSOR_SHELL"></a>

## 160.62 `CONFIG_SENSOR_SHELL`

**提示（Prompt）**：传感器命令行（Sensor Shell）

**说明（Help）**

此命令行（Shell）提供对基本传感器数据的访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_CBPRINTF_FP_SUPPORT
CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_CBPRINTF_FP_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CBPRINTF_FP_SUPPORT)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_SENSOR_SHELL_BATTERY"></a>

## 160.63 `CONFIG_SENSOR_SHELL_BATTERY`

**提示（Prompt）**：传感器命令行的 `battery` 命令

**说明（Help）**

启用 `battery` 命令，以便于阅读的格式报告充电信息。该命令使用电量计（Fuel Gauge）读取相关信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SENSOR_SHELL_MAX_TRIGGER_DEVICES"></a>

## 160.64 `CONFIG_SENSOR_SHELL_MAX_TRIGGER_DEVICES`

**提示（Prompt）**：命令行中可启用触发器的传感器设备最大数量

**说明（Help）**

命令行（Shell）命令可为其启用触发器（Trigger）的传感器设备最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR_SHELL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/sensor/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_SHELL`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_SHELL)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SENSOR_SHELL_STREAM"></a>

## 160.65 `CONFIG_SENSOR_SHELL_STREAM`

**提示（Prompt）**：传感器命令行的 `stream` 命令

**说明（Help）**

向传感器命令行（Sensor Shell）添加 `stream` 子命令。在支持流式传输（Streaming）的驱动上运行时，命令行持续打印新到达的值，直到数据流关闭；这类驱动通常由硬件 FIFO 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR_SHELL && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 传感器命令行（Sensor Shell）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_SHELL`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_SHELL)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SENSOR_SHELL_THREAD_STACK_SIZE"></a>

## 160.66 `CONFIG_SENSOR_SHELL_THREAD_STACK_SIZE`

**提示（Prompt）**：传感器命令行数据处理线程的栈大小

**说明（Help）**

传感器命令行（Sensor Shell）使用专用线程处理传感器在单次模式（One-shot Mode）或流式模式（Streaming Mode）下送来的数据。此配置控制该线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR_SHELL_STREAM && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → 传感器命令行（Sensor Shell） → 传感器命令行的 `stream` 命令

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_SHELL_STREAM`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_SHELL_STREAM)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SENSOR_SHELL_TRIG_PRINT_TIMEOUT_MS"></a>

## 160.67 `CONFIG_SENSOR_SHELL_TRIG_PRINT_TIMEOUT_MS`

**提示（Prompt）**：打印传感器采样平均值的超时时间

**说明（Help）**

控制采样窗口（Sampling Window）的频率，传感器中断处理程序在该窗口内收集数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR_SHELL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`drivers/sensor/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_SHELL`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_SHELL)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SF32LB_TSEN"></a>

## 160.68 `CONFIG_SF32LB_TSEN`

**提示（Prompt）**：SIFLI SF32LB TSEN 温度传感器驱动

**说明（Help）**

启用 SIFLI SF32LB 片上温度传感器（On-chip Temperature Sensor，TSEN）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_TSEN_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/sifli/sf32lb_tsen/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sifli/sf32lb_tsen/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SGP40"></a>

## 160.69 `CONFIG_SGP40`

**提示（Prompt）**：SGP40 多像素气体传感器（Multipixel Gas Sensor）

**说明（Help）**

启用 SGP40 多像素气体传感器（Multipixel Gas Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SENSIRION_SGP40_ENABLED && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/sensirion/sgp40/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sgp40/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_SHT3XD"></a>

## 160.70 `CONFIG_SHT3XD`

**提示（Prompt）**：SHT3xD 温湿度传感器（Temperature and Humidity Sensor）

**说明（Help）**

启用 SHT3xD 温湿度传感器（Temperature and Humidity Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SENSIRION_SHT3XD_ENABLED && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_SHT3XD_MEASUREMENT_MODE"></a>

## 160.71 `CONFIG_SHT3XD_MEASUREMENT_MODE`

**提示（Prompt）**：测量模式（Measurement Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHT3XD && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_SHT3XD_PERIODIC_MODE
```

**可选项（Choices）**

```text
CONFIG_SHT3XD_SINGLE_SHOT_MODE
CONFIG_SHT3XD_PERIODIC_MODE
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SHT3XD_PERIODIC_MODE`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_PERIODIC_MODE)、[`CONFIG_SHT3XD_SINGLE_SHOT_MODE`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_SINGLE_SHOT_MODE)。

<a id="CONFIG_SHT3XD_MPS"></a>

## 160.72 `CONFIG_SHT3XD_MPS`

**提示（Prompt）**：每秒测量次数（Measurements per Second）

**说明（Help）**

每秒执行的测量次数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHT3XD_PERIODIC_MODE && CONFIG_SHT3XD && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_SHT3XD_MPS_1
```

**可选项（Choices）**

```text
CONFIG_SHT3XD_MPS_05
CONFIG_SHT3XD_MPS_1
CONFIG_SHT3XD_MPS_2
CONFIG_SHT3XD_MPS_4
CONFIG_SHT3XD_MPS_10
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_PERIODIC_MODE`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_PERIODIC_MODE)、[`CONFIG_SHT3XD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SHT3XD_MPS_1`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_MPS_1)、[`CONFIG_SHT3XD_MPS_05`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_MPS_05)、[`CONFIG_SHT3XD_MPS_2`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_MPS_2)、[`CONFIG_SHT3XD_MPS_4`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_MPS_4)、[`CONFIG_SHT3XD_MPS_10`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_MPS_10)。

<a id="CONFIG_SHT3XD_MPS_05"></a>

## 160.73 `CONFIG_SHT3XD_MPS_05`

**提示（Prompt）**：0.5

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHT3XD_MPS>
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor） → 每秒测量次数（Measurements per Second）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_MPS`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_MPS)。

<a id="CONFIG_SHT3XD_MPS_1"></a>

## 160.74 `CONFIG_SHT3XD_MPS_1`

**提示（Prompt）**：1

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHT3XD_MPS>
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor） → 每秒测量次数（Measurements per Second）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_MPS`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_MPS)。

<a id="CONFIG_SHT3XD_MPS_10"></a>

## 160.75 `CONFIG_SHT3XD_MPS_10`

**提示（Prompt）**：10

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHT3XD_MPS>
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor） → 每秒测量次数（Measurements per Second）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_MPS`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_MPS)。

<a id="CONFIG_SHT3XD_MPS_2"></a>

## 160.76 `CONFIG_SHT3XD_MPS_2`

**提示（Prompt）**：2

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHT3XD_MPS>
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor） → 每秒测量次数（Measurements per Second）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_MPS`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_MPS)。

<a id="CONFIG_SHT3XD_MPS_4"></a>

## 160.77 `CONFIG_SHT3XD_MPS_4`

**提示（Prompt）**：4

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHT3XD_MPS>
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor） → 每秒测量次数（Measurements per Second）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_MPS`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_MPS)。

<a id="CONFIG_SHT3XD_PERIODIC_MODE"></a>

## 160.78 `CONFIG_SHT3XD_PERIODIC_MODE`

**提示（Prompt）**：周期性数据采集（Periodic Data Acquisition）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHT3XD_MEASUREMENT_MODE>
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor） → 测量模式（Measurement Mode）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_MEASUREMENT_MODE`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_MEASUREMENT_MODE)。

<a id="CONFIG_SHT3XD_REPEATABILITY"></a>

## 160.79 `CONFIG_SHT3XD_REPEATABILITY`

**提示（Prompt）**：测量重复性（Measurement Repeatability）

**说明（Help）**

不同重复性模式（Repeatability Mode）在测量耗时、噪声水平和能耗方面有所不同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHT3XD && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_SHT3XD_REPEATABILITY_HIGH
```

**可选项（Choices）**

```text
CONFIG_SHT3XD_REPEATABILITY_LOW
CONFIG_SHT3XD_REPEATABILITY_MEDIUM
CONFIG_SHT3XD_REPEATABILITY_HIGH
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SHT3XD_REPEATABILITY_HIGH`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_REPEATABILITY_HIGH)、[`CONFIG_SHT3XD_REPEATABILITY_LOW`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_REPEATABILITY_LOW)、[`CONFIG_SHT3XD_REPEATABILITY_MEDIUM`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_REPEATABILITY_MEDIUM)。

<a id="CONFIG_SHT3XD_REPEATABILITY_HIGH"></a>

## 160.80 `CONFIG_SHT3XD_REPEATABILITY_HIGH`

**提示（Prompt）**：高（High）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHT3XD_REPEATABILITY>
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor） → 测量重复性（Measurement Repeatability）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_REPEATABILITY`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_REPEATABILITY)。

<a id="CONFIG_SHT3XD_REPEATABILITY_LOW"></a>

## 160.81 `CONFIG_SHT3XD_REPEATABILITY_LOW`

**提示（Prompt）**：低（Low）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHT3XD_REPEATABILITY>
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor） → 测量重复性（Measurement Repeatability）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_REPEATABILITY`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_REPEATABILITY)。

<a id="CONFIG_SHT3XD_REPEATABILITY_MEDIUM"></a>

## 160.82 `CONFIG_SHT3XD_REPEATABILITY_MEDIUM`

**提示（Prompt）**：中（Medium）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHT3XD_REPEATABILITY>
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor） → 测量重复性（Measurement Repeatability）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_REPEATABILITY`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_REPEATABILITY)。

<a id="CONFIG_SHT3XD_SINGLE_SHOT_MODE"></a>

## 160.83 `CONFIG_SHT3XD_SINGLE_SHOT_MODE`

**提示（Prompt）**：单次（Single Shot）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHT3XD_MEASUREMENT_MODE>
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor） → 测量模式（Measurement Mode）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_MEASUREMENT_MODE`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_MEASUREMENT_MODE)。

<a id="CONFIG_SHT3XD_THREAD_PRIORITY"></a>

## 160.84 `CONFIG_SHT3XD_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHT3XD_TRIGGER_OWN_THREAD && CONFIG_SHT3XD && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_TRIGGER_OWN_THREAD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_TRIGGER_OWN_THREAD)、[`CONFIG_SHT3XD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SHT3XD_THREAD_STACK_SIZE"></a>

## 160.85 `CONFIG_SHT3XD_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHT3XD_TRIGGER_OWN_THREAD && CONFIG_SHT3XD && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_TRIGGER_OWN_THREAD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_TRIGGER_OWN_THREAD)、[`CONFIG_SHT3XD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SHT3XD_TRIGGER_GLOBAL_THREAD"></a>

## 160.86 `CONFIG_SHT3XD_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_SHT3XD_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHT3XD_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SHT3XD_TRIGGER`。

<a id="CONFIG_SHT3XD_TRIGGER_MODE"></a>

## 160.87 `CONFIG_SHT3XD_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHT3XD && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_SHT3XD_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_SHT3XD_TRIGGER_NONE
CONFIG_SHT3XD_TRIGGER_GLOBAL_THREAD
CONFIG_SHT3XD_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SHT3XD_TRIGGER_NONE`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_TRIGGER_NONE)、[`CONFIG_SHT3XD_TRIGGER_GLOBAL_THREAD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_TRIGGER_GLOBAL_THREAD)、[`CONFIG_SHT3XD_TRIGGER_OWN_THREAD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_TRIGGER_OWN_THREAD)。

<a id="CONFIG_SHT3XD_TRIGGER_NONE"></a>

## 160.88 `CONFIG_SHT3XD_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHT3XD_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_TRIGGER_MODE`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD_TRIGGER_MODE)。

<a id="CONFIG_SHT3XD_TRIGGER_OWN_THREAD"></a>

## 160.89 `CONFIG_SHT3XD_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_SHT3XD_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/sensirion/sht3xd/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht3xd/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SHT3xD 温湿度传感器（Temperature and Humidity Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_SHT3XD_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHT3XD_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SHT3XD_TRIGGER`。

<a id="CONFIG_SHT4X"></a>

## 160.90 `CONFIG_SHT4X`

**提示（Prompt）**：SHT4x 温湿度传感器（Temperature and Humidity Sensor）

**说明（Help）**

启用 SHT4x 温湿度传感器（Temperature and Humidity Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SENSIRION_SHT4X_ENABLED && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/sensirion/sht4x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/sht4x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_SHTCX"></a>

## 160.91 `CONFIG_SHTCX`

**提示（Prompt）**：SHTCX：SHTC1 和 SHTC3 温湿度传感器

**说明（Help）**

启用 SHTC1 和 SHTC3 温湿度传感器（Temperature and Humidity Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SENSIRION_SHTCX_ENABLED && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/sensirion/shtcx/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/sensirion/shtcx/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_SI7006"></a>

## 160.92 `CONFIG_SI7006`

**提示（Prompt）**：SHT21、Si7006 和 HTU21D 温湿度传感器

**说明（Help）**

为多种兼容 Sensirion SHT21 的温湿度传感器（Humidity and Temperature Sensor）启用基于 I2C 的驱动，例如 Silicon Labs Si7006/13/20/21 和 Measurement Specialties HTU21D。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_SILABS_SI7006_ENABLED || DT_HAS_SENSIRION_SHT21_ENABLED || DT_HAS_MEAS_HTU21D_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_REGULATOR if n
```

**定义位置（Location）**：[`drivers/sensor/silabs/si7006/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/silabs/si7006/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_SI7055"></a>

## 160.93 `CONFIG_SI7055`

**提示（Prompt）**：Si7055 温度传感器（Temperature Sensor）

**说明（Help）**

启用基于 I2C 的 Si7055 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SI7055_ENABLED && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/silabs/si7055/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/silabs/si7055/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_SI7055_ENABLE_CHECKSUM"></a>

## 160.94 `CONFIG_SI7055_ENABLE_CHECKSUM`

**提示（Prompt）**：SI7055 测量校验和（Checksum on Measurement）

**说明（Help）**

验证温度测量数据附带的额外校验和字节（Checksum Byte）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SI7055 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/silabs/si7055/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/silabs/si7055/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Si7055 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_SI7055`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SI7055)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SI7060"></a>

## 160.95 `CONFIG_SI7060`

**提示（Prompt）**：SI7060 温度传感器（Temperature Sensor）

**说明（Help）**

启用 SI7060 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SI7060_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/silabs/si7060/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/silabs/si7060/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_SI7210"></a>

## 160.96 `CONFIG_SI7210`

**提示（Prompt）**：Si7210 霍尔效应磁位置与温度传感器

**说明（Help）**

启用 Si7210 霍尔效应磁位置与温度传感器（Hall Effect Magnetic Position and Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SI7210_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/silabs/si7210/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/silabs/si7210/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_SM351LT"></a>

## 160.97 `CONFIG_SM351LT`

**提示（Prompt）**：SM351LT 磁阻传感器（Magnetoresistive Sensor）

**说明（Help）**

启用基于 GPIO 的 SM351LT 磁阻传感器（Magnetoresistive Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HONEYWELL_SM351LT_ENABLED && CONFIG_GPIO && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/honeywell/sm351lt/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/sm351lt/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SM351LT_THREAD_PRIORITY"></a>

## 160.98 `CONFIG_SM351LT_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SM351LT_TRIGGER_OWN_THREAD && CONFIG_SM351LT && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/honeywell/sm351lt/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/sm351lt/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SM351LT 磁阻传感器（Magnetoresistive Sensor）

**配置项引用（Symbol References）**：[`CONFIG_SM351LT_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_SM351LT_TRIGGER_OWN_THREAD)、[`CONFIG_SM351LT`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SM351LT)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SM351LT_THREAD_STACK_SIZE"></a>

## 160.99 `CONFIG_SM351LT_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SM351LT_TRIGGER_OWN_THREAD && CONFIG_SM351LT && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/sensor/honeywell/sm351lt/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/sm351lt/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SM351LT 磁阻传感器（Magnetoresistive Sensor）

**配置项引用（Symbol References）**：[`CONFIG_SM351LT_TRIGGER_OWN_THREAD`](P161_drivers_sensor_配置项参考_13.md#CONFIG_SM351LT_TRIGGER_OWN_THREAD)、[`CONFIG_SM351LT`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SM351LT)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_SM351LT_TRIGGER_GLOBAL_THREAD"></a>

## 160.100 `CONFIG_SM351LT_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

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

**定义位置（Location）**：[`drivers/sensor/honeywell/sm351lt/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/honeywell/sm351lt/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → SM351LT 磁阻传感器（Magnetoresistive Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_SM351LT_TRIGGER_MODE`](P161_drivers_sensor_配置项参考_13.md#CONFIG_SM351LT_TRIGGER_MODE)、[`CONFIG_SM351LT_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SM351LT_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SM351LT_TRIGGER`。

<!-- kconfig-navigation -->

[上一章](P159_drivers_sensor_配置项参考_11.md) · [返回大纲](大纲.md) · [下一章](P161_drivers_sensor_配置项参考_13.md)
