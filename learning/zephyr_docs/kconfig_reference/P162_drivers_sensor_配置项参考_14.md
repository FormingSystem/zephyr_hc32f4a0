---
id: learning.zephyr-docs.kconfig-reference.page-162
title: "`drivers/sensor`配置项参考（14/15）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第162章\_`drivers/sensor`配置项参考（14/15）

本章翻译官方 Kconfig 数据库中 `drivers/sensor` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_TMD2620_TRIGGER_GLOBAL_THREAD"></a>

## 162.1 `CONFIG_TMD2620_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_TMD2620_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ams/tmd2620/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tmd2620/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → OSRAM-AMS TMD2620 接近传感器（Proximity Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TMD2620_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMD2620_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMD2620_TRIGGER`。

<a id="CONFIG_TMD2620_TRIGGER_NONE"></a>

## 162.2 `CONFIG_TMD2620_TRIGGER_NONE`

**提示（Prompt）**：无触发器（No Trigger）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/ams/tmd2620/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tmd2620/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → OSRAM-AMS TMD2620 接近传感器（Proximity Sensor） → 触发模式（Trigger Mode）

<a id="CONFIG_TMP007"></a>

## 162.3 `CONFIG_TMP007`

**提示（Prompt）**：TMP007 红外热电堆传感器（Infrared Thermopile Sensor）

**说明（Help）**

启用 TMP007 红外热电堆传感器（Infrared Thermopile Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TMP007_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp007/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp007/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TMP007_THREAD_PRIORITY"></a>

## 162.4 `CONFIG_TMP007_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TMP007_TRIGGER_OWN_THREAD && CONFIG_TMP007 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp007/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp007/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP007 红外热电堆传感器（Infrared Thermopile Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TMP007_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP007_TRIGGER_OWN_THREAD)、[`CONFIG_TMP007`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP007)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TMP007_THREAD_STACK_SIZE"></a>

## 162.5 `CONFIG_TMP007_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TMP007_TRIGGER_OWN_THREAD && CONFIG_TMP007 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp007/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp007/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP007 红外热电堆传感器（Infrared Thermopile Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TMP007_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP007_TRIGGER_OWN_THREAD)、[`CONFIG_TMP007`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP007)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TMP007_TRIGGER_GLOBAL_THREAD"></a>

## 162.6 `CONFIG_TMP007_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_TMP007_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp007/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp007/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP007 红外热电堆传感器（Infrared Thermopile Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TMP007_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP007_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMP007_TRIGGER`。

<a id="CONFIG_TMP007_TRIGGER_NONE"></a>

## 162.7 `CONFIG_TMP007_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp007/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp007/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP007 红外热电堆传感器（Infrared Thermopile Sensor） → 触发模式（Trigger Mode）

<a id="CONFIG_TMP007_TRIGGER_OWN_THREAD"></a>

## 162.8 `CONFIG_TMP007_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_TMP007_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp007/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp007/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP007 红外热电堆传感器（Infrared Thermopile Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TMP007_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP007_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMP007_TRIGGER`。

<a id="CONFIG_TMP1075"></a>

## 162.9 `CONFIG_TMP1075`

**提示（Prompt）**：TMP1075 温度传感器（Temperature Sensor）

**说明（Help）**

启用 Texas Instruments TMP1075 高准确度数字温度传感器（High-Accuracy Digital Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TMP1075_ENABLED && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/ti/tmp1075/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp1075/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_TMP1075_ALERT_INTERRUPTS"></a>

## 162.10 `CONFIG_TMP1075_ALERT_INTERRUPTS`

**提示（Prompt）**：允许使用中断处理过温和欠温警报

**说明（Help）**

配置中断以处理欠温和过温警报（Under/Over Temperature Alert）。有关其工作方式的更多信息，请参阅 TMP1075 规格说明书。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TMP1075 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp1075/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp1075/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP1075 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TMP1075`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP1075)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TMP108"></a>

## 162.11 `CONFIG_TMP108`

**提示（Prompt）**：TMP108 温度传感器（Temperature Sensor）

**说明（Help）**

启用 TMP108 温度传感器及／或其变体 AMS AS621x、AS6221 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_TI_TMP108_ENABLED || DT_HAS_AMS_AS6212_ENABLED || DT_HAS_AMS_AS6221_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp108/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp108/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TMP108_ALERT_INTERRUPTS"></a>

## 162.12 `CONFIG_TMP108_ALERT_INTERRUPTS`

**提示（Prompt）**：允许使用中断处理过温和欠温警报

**说明（Help）**

配置中断以处理欠温和过温警报（Under/Over Temperature Alert）。有关其工作方式的更多信息，请参阅 TMP108 规格说明书。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TMP108 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp108/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp108/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP108 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TMP108`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP108)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TMP112"></a>

## 162.13 `CONFIG_TMP112`

**提示（Prompt）**：TMP112 温度传感器（Temperature Sensor）

**说明（Help）**

启用 Texas Instruments TMP112 高准确度数字温度传感器（High-Accuracy Digital Temperature Sensor）驱动。TMP102 与 TMP112 兼容，但准确度较低，已使用此驱动成功完成测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TMP112_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp112/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp112/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TMP112_FULL_SCALE_RUNTIME"></a>

## 162.14 `CONFIG_TMP112_FULL_SCALE_RUNTIME`

**提示（Prompt）**：允许运行时设置扩展模式（Extended Mode）

**说明（Help）**

启用后，可通过 `tmp112_attr_set`，使用 `SENSOR_ATTR_FULL_SCALE` 属性并将值设为 128 或 150，选择扩展模式（Extended Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TMP112 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp112/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp112/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP112 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TMP112`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP112)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TMP112_SAMPLING_FREQUENCY_RUNTIME"></a>

## 162.15 `CONFIG_TMP112_SAMPLING_FREQUENCY_RUNTIME`

**提示（Prompt）**：允许运行时设置转换速率（Conversion Rate）

**说明（Help）**

启用后，可在运行时通过 `sensor_attr_set` 和 `SENSOR_ATTR_SAMPLING_FREQUENCY` 属性设置转换速率（Conversion Rate）。运行时将速率设为 0 Hz，会使传感器进入关断／单次模式（Shutdown/One-shot Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TMP112 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp112/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp112/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP112 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TMP112`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP112)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TMP114"></a>

## 162.16 `CONFIG_TMP114`

**提示（Prompt）**：TMP114 温度传感器（Temperature Sensor）

**说明（Help）**

启用 TMP114 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TMP114_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp114/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp114/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TMP11X"></a>

## 162.17 `CONFIG_TMP11X`

**提示（Prompt）**：TMP116、TMP117 和 TMP119 温度传感器

**说明（Help）**

启用 TMP116、TMP117 和 TMP119 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TMP11X_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp11x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp11x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TMP11X_THREAD_PRIORITY"></a>

## 162.18 `CONFIG_TMP11X_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TMP11X_TRIGGER_OWN_THREAD && CONFIG_TMP11X_TRIGGER && CONFIG_TMP11X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP116、TMP117 和 TMP119 温度传感器

**配置项引用（Symbol References）**：[`CONFIG_TMP11X_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP11X_TRIGGER_OWN_THREAD)、[`CONFIG_TMP11X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP11X_TRIGGER)、[`CONFIG_TMP11X`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP11X)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMP11X_TRIGGER`。

<a id="CONFIG_TMP11X_THREAD_STACK_SIZE"></a>

## 162.19 `CONFIG_TMP11X_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TMP11X_TRIGGER_OWN_THREAD && CONFIG_TMP11X_TRIGGER && CONFIG_TMP11X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP116、TMP117 和 TMP119 温度传感器

**配置项引用（Symbol References）**：[`CONFIG_TMP11X_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP11X_TRIGGER_OWN_THREAD)、[`CONFIG_TMP11X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP11X_TRIGGER)、[`CONFIG_TMP11X`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP11X)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMP11X_TRIGGER`。

<a id="CONFIG_TMP11X_TRIGGER_GLOBAL_THREAD"></a>

## 162.20 `CONFIG_TMP11X_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_TMP11X_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_TMP11X_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP116、TMP117 和 TMP119 温度传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_TMP11X_TRIGGER_MODE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP11X_TRIGGER_MODE)、[`CONFIG_TMP11X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP11X_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMP11X_TRIGGER`。

<a id="CONFIG_TMP11X_TRIGGER_MODE"></a>

## 162.21 `CONFIG_TMP11X_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定传感器模块使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TMP11X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_TMP11X_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_TMP11X_TRIGGER_NONE
CONFIG_TMP11X_TRIGGER_GLOBAL_THREAD
CONFIG_TMP11X_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP116、TMP117 和 TMP119 温度传感器

**配置项引用（Symbol References）**：[`CONFIG_TMP11X`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP11X)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_TMP11X_TRIGGER_NONE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP11X_TRIGGER_NONE)、[`CONFIG_TMP11X_TRIGGER_GLOBAL_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP11X_TRIGGER_GLOBAL_THREAD)、[`CONFIG_TMP11X_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP11X_TRIGGER_OWN_THREAD)。

<a id="CONFIG_TMP11X_TRIGGER_NONE"></a>

## 162.22 `CONFIG_TMP11X_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TMP11X_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP116、TMP117 和 TMP119 温度传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TMP11X_TRIGGER_MODE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP11X_TRIGGER_MODE)。

<a id="CONFIG_TMP11X_TRIGGER_OWN_THREAD"></a>

## 162.23 `CONFIG_TMP11X_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_TMP11X_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_TMP11X_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP116、TMP117 和 TMP119 温度传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_TMP11X_TRIGGER_MODE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP11X_TRIGGER_MODE)、[`CONFIG_TMP11X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP11X_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMP11X_TRIGGER`。

<a id="CONFIG_TMP435"></a>

## 162.24 `CONFIG_TMP435`

**提示（Prompt）**：TMP435 温度传感器（Temperature Sensor）

**说明（Help）**

启用 TMP435 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TMP435_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp435/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp435/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TMP451"></a>

## 162.25 `CONFIG_TMP451`

**提示（Prompt）**：TMP451 温度传感器（Temperature Sensor）驱动

**说明（Help）**

启用 TMP451 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TMP451_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/tmp451/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/tmp451/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TMP451_THREAD_PRIORITY"></a>

## 162.26 `CONFIG_TMP451_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TMP451_TRIGGER_OWN_THREAD && CONFIG_TMP451_TRIGGER && CONFIG_TMP451 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP451 温度传感器（Temperature Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_TMP451_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP451_TRIGGER_OWN_THREAD)、[`CONFIG_TMP451_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP451_TRIGGER)、[`CONFIG_TMP451`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP451)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMP451_TRIGGER`。

<a id="CONFIG_TMP451_THREAD_STACK_SIZE"></a>

## 162.27 `CONFIG_TMP451_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TMP451_TRIGGER_OWN_THREAD && CONFIG_TMP451_TRIGGER && CONFIG_TMP451 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP451 温度传感器（Temperature Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_TMP451_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP451_TRIGGER_OWN_THREAD)、[`CONFIG_TMP451_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP451_TRIGGER)、[`CONFIG_TMP451`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP451)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMP451_TRIGGER`。

<a id="CONFIG_TMP451_TRIGGER_GLOBAL_THREAD"></a>

## 162.28 `CONFIG_TMP451_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_TMP451_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_TMP451_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP451 温度传感器（Temperature Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_TMP451_TRIGGER_MODE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP451_TRIGGER_MODE)、[`CONFIG_TMP451_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP451_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMP451_TRIGGER`。

<a id="CONFIG_TMP451_TRIGGER_MODE"></a>

## 162.29 `CONFIG_TMP451_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定传感器模块使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TMP451 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_TMP451_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_TMP451_TRIGGER_NONE
CONFIG_TMP451_TRIGGER_GLOBAL_THREAD
CONFIG_TMP451_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP451 温度传感器（Temperature Sensor）驱动

**配置项引用（Symbol References）**：[`CONFIG_TMP451`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP451)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_TMP451_TRIGGER_NONE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP451_TRIGGER_NONE)、[`CONFIG_TMP451_TRIGGER_GLOBAL_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP451_TRIGGER_GLOBAL_THREAD)、[`CONFIG_TMP451_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP451_TRIGGER_OWN_THREAD)。

<a id="CONFIG_TMP451_TRIGGER_NONE"></a>

## 162.30 `CONFIG_TMP451_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TMP451_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP451 温度传感器（Temperature Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TMP451_TRIGGER_MODE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP451_TRIGGER_MODE)。

<a id="CONFIG_TMP451_TRIGGER_OWN_THREAD"></a>

## 162.31 `CONFIG_TMP451_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_TMP451_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_TMP451_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TMP451 温度传感器（Temperature Sensor）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_TMP451_TRIGGER_MODE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TMP451_TRIGGER_MODE)、[`CONFIG_TMP451_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TMP451_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TMP451_TRIGGER`。

<a id="CONFIG_TSIC_XX6"></a>

## 162.32 `CONFIG_TSIC_XX6`

**提示（Prompt）**：TSic xx6 驱动

**说明（Help）**

启用 TSic 206/306/316/506F/516/716 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_IST_TSIC_XX6_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PWM
CONFIG_PWM_CAPTURE
```

**定义位置（Location）**：[`drivers/sensor/tsic_xx6/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tsic_xx6/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_PWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM)、[`CONFIG_PWM_CAPTURE`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_CAPTURE)。

<a id="CONFIG_TSL2540"></a>

## 162.33 `CONFIG_TSL2540`

**提示（Prompt）**：TSL2540 环境光传感器（Ambient Light Sensor）

**说明（Help）**

启用 TSL2540 传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMS_TSL2540_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ams/tsl2540/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tsl2540/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TSL2540_THREAD_PRIORITY"></a>

## 162.34 `CONFIG_TSL2540_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TSL2540_TRIGGER_OWN_THREAD && CONFIG_TSL2540 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/ams/tsl2540/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tsl2540/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TSL2540 环境光传感器（Ambient Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TSL2540_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TSL2540_TRIGGER_OWN_THREAD)、[`CONFIG_TSL2540`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TSL2540)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TSL2540_THREAD_STACK_SIZE"></a>

## 162.35 `CONFIG_TSL2540_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TSL2540_TRIGGER_OWN_THREAD && CONFIG_TSL2540 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/ams/tsl2540/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tsl2540/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TSL2540 环境光传感器（Ambient Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TSL2540_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TSL2540_TRIGGER_OWN_THREAD)、[`CONFIG_TSL2540`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TSL2540)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TSL2540_TRIGGER_GLOBAL_THREAD"></a>

## 162.36 `CONFIG_TSL2540_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_TSL2540_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ams/tsl2540/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tsl2540/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TSL2540 环境光传感器（Ambient Light Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TSL2540_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TSL2540_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TSL2540_TRIGGER`。

<a id="CONFIG_TSL2540_TRIGGER_NONE"></a>

## 162.37 `CONFIG_TSL2540_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/ams/tsl2540/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tsl2540/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TSL2540 环境光传感器（Ambient Light Sensor） → 触发模式（Trigger Mode）

<a id="CONFIG_TSL2540_TRIGGER_OWN_THREAD"></a>

## 162.38 `CONFIG_TSL2540_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_TSL2540_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ams/tsl2540/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tsl2540/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → TSL2540 环境光传感器（Ambient Light Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TSL2540_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TSL2540_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TSL2540_TRIGGER`。

<a id="CONFIG_TSL2561"></a>

## 162.39 `CONFIG_TSL2561`

**提示（Prompt）**：OSRAM-AMS TSL2561 光照传感器（Light Sensor）

**说明（Help）**

启用 TSL2561 传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMS_TSL2561_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ams/tsl2561/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tsl2561/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TSL2591"></a>

## 162.40 `CONFIG_TSL2591`

**提示（Prompt）**：OSRAM-AMS TSL2591 光照传感器（Light Sensor）

**说明（Help）**

启用 TSL2591 传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMS_TSL2591_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ams/tsl2591/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tsl2591/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_TSL2591_FETCH_WAIT"></a>

## 162.41 `CONFIG_TSL2591_FETCH_WAIT`

**提示（Prompt）**：获取前等待有效的传感器读数

**说明（Help）**

启用后，驱动在获取（Fetch）调用期间，如有必要，会自动等待一个积分周期（Integration Cycle）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TSL2591 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/ams/tsl2591/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tsl2591/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → OSRAM-AMS TSL2591 光照传感器（Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TSL2591`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TSL2591)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TSL2591_THREAD_PRIORITY"></a>

## 162.42 `CONFIG_TSL2591_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TSL2591_TRIGGER_OWN_THREAD && CONFIG_TSL2591 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/ams/tsl2591/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tsl2591/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → OSRAM-AMS TSL2591 光照传感器（Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TSL2591_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TSL2591_TRIGGER_OWN_THREAD)、[`CONFIG_TSL2591`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TSL2591)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TSL2591_THREAD_STACK_SIZE"></a>

## 162.43 `CONFIG_TSL2591_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TSL2591_TRIGGER_OWN_THREAD && CONFIG_TSL2591 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/ams/tsl2591/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tsl2591/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → OSRAM-AMS TSL2591 光照传感器（Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TSL2591_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TSL2591_TRIGGER_OWN_THREAD)、[`CONFIG_TSL2591`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TSL2591)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_TSL2591_TRIGGER_GLOBAL_THREAD"></a>

## 162.44 `CONFIG_TSL2591_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_TSL2591_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ams/tsl2591/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tsl2591/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → OSRAM-AMS TSL2591 光照传感器（Light Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TSL2591_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TSL2591_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TSL2591_TRIGGER`。

<a id="CONFIG_TSL2591_TRIGGER_NONE"></a>

## 162.45 `CONFIG_TSL2591_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/ams/tsl2591/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tsl2591/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → OSRAM-AMS TSL2591 光照传感器（Light Sensor） → 触发模式（Trigger Mode）

<a id="CONFIG_TSL2591_TRIGGER_OWN_THREAD"></a>

## 162.46 `CONFIG_TSL2591_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_TSL2591_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ams/tsl2591/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tsl2591/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → OSRAM-AMS TSL2591 光照传感器（Light Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_TSL2591_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TSL2591_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TSL2591_TRIGGER`。

<a id="CONFIG_TSL2591_WARN_SATURATED"></a>

## 162.47 `CONFIG_TSL2591_WARN_SATURATED`

**提示（Prompt）**：传感器可能饱和时发出警告

**说明（Help）**

启用后，如果数据获取后传感器的模数转换器（ADC）可能处于饱和状态（Saturation），驱动将发出警告。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TSL2591 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/ams/tsl2591/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/tsl2591/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → OSRAM-AMS TSL2591 光照传感器（Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_TSL2591`](P162_drivers_sensor_配置项参考_14.md#CONFIG_TSL2591)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_VCMP_IT8XXX2"></a>

## 162.48 `CONFIG_VCMP_IT8XXX2`

**提示（Prompt）**：ITE it8xxx2 电压比较器（Voltage Comparator）

**说明（Help）**

此选项启用 ITE it8xxx2 电压比较器（Voltage Comparator）。it8xxx2 支持六个分辨率为 10 位的电压比较器通道，每个比较器的输入来自 ADC 引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_VCMP_ENABLED && CONFIG_SOC_IT8XXX2 && CONFIG_ADC_ITE_IT8XXX2 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/ite/ite_vcmp_it8xxx2/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ite/ite_vcmp_it8xxx2/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2)、[`CONFIG_ADC_ITE_IT8XXX2`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ITE_IT8XXX2)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_IT8XXX2`。

<a id="CONFIG_VCMP_IT8XXX2_INIT_PRIORITY"></a>

## 162.49 `CONFIG_VCMP_IT8XXX2_INIT_PRIORITY`

**提示（Prompt）**：ITE it8xxx2 电压比较器设备实例初始化优先级

**说明（Help）**

此选项设置 ITE 电压比较器设备实例的初始化优先级（Init Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VCMP_IT8XXX2 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_SENSOR_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/sensor/ite/ite_vcmp_it8xxx2/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ite/ite_vcmp_it8xxx2/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ITE it8xxx2 电压比较器（Voltage Comparator）

**配置项引用（Symbol References）**：[`CONFIG_VCMP_IT8XXX2`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCMP_IT8XXX2)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SENSOR_INIT_PRIORITY`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_INIT_PRIORITY)。

<a id="CONFIG_VCMP_IT8XXX2_WORKQUEUE"></a>

## 162.50 `CONFIG_VCMP_IT8XXX2_WORKQUEUE`

**提示（Prompt）**：ITE it8xxx2 电压比较器阈值检测使用内部工作队列（Internal Work Queue）

**说明（Help）**

阈值检测中断服务例程（ISR）利用系统工作队列调用触发处理程序；设置此选项可改用专用工作队列。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_VCMP_IT8XXX2 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/ite/ite_vcmp_it8xxx2/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ite/ite_vcmp_it8xxx2/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ITE it8xxx2 电压比较器（Voltage Comparator）

**配置项引用（Symbol References）**：[`CONFIG_VCMP_IT8XXX2`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCMP_IT8XXX2)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_VCMP_IT8XXX2_WORKQUEUE_PRIORITY"></a>

## 162.51 `CONFIG_VCMP_IT8XXX2_WORKQUEUE_PRIORITY`

**提示（Prompt）**：ITE it8xxx2 电压比较器阈值检测工作队列优先级

**说明（Help）**

此选项设置 ITE 电压比较器内部阈值检测工作队列（Workqueue）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VCMP_IT8XXX2_WORKQUEUE && CONFIG_VCMP_IT8XXX2 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_SYSTEM_WORKQUEUE_PRIORITY
```

**定义位置（Location）**：[`drivers/sensor/ite/ite_vcmp_it8xxx2/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ite/ite_vcmp_it8xxx2/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ITE it8xxx2 电压比较器（Voltage Comparator） → ITE it8xxx2 电压比较器阈值检测使用内部工作队列（Internal Work Queue）

**配置项引用（Symbol References）**：[`CONFIG_VCMP_IT8XXX2_WORKQUEUE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCMP_IT8XXX2_WORKQUEUE)、[`CONFIG_VCMP_IT8XXX2`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCMP_IT8XXX2)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SYSTEM_WORKQUEUE_PRIORITY`](P002_kernel_配置项参考_2.md#CONFIG_SYSTEM_WORKQUEUE_PRIORITY)。

<a id="CONFIG_VCMP_IT8XXX2_WORKQUEUE_STACK_SIZE"></a>

## 162.52 `CONFIG_VCMP_IT8XXX2_WORKQUEUE_STACK_SIZE`

**提示（Prompt）**：ITE it8xxx2 电压比较器阈值检测工作队列栈大小

**说明（Help）**

此选项设置 ITE 电压比较器内部阈值检测工作队列（Workqueue）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VCMP_IT8XXX2_WORKQUEUE && CONFIG_VCMP_IT8XXX2 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
768
```

**定义位置（Location）**：[`drivers/sensor/ite/ite_vcmp_it8xxx2/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ite/ite_vcmp_it8xxx2/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ITE it8xxx2 电压比较器（Voltage Comparator） → ITE it8xxx2 电压比较器阈值检测使用内部工作队列（Internal Work Queue）

**配置项引用（Symbol References）**：[`CONFIG_VCMP_IT8XXX2_WORKQUEUE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCMP_IT8XXX2_WORKQUEUE)、[`CONFIG_VCMP_IT8XXX2`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCMP_IT8XXX2)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_VCNL36825T"></a>

## 162.53 `CONFIG_VCNL36825T`

**提示（Prompt）**：VCNL36825T 接近传感器（Proximity Sensor）

**说明（Help）**

启用 VCNL36825T 传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VISHAY_VCNL36825T_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/vishay/vcnl36825t/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl36825t/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_VCNL36825T_THREAD_PRIORITY"></a>

## 162.54 `CONFIG_VCNL36825T_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VCNL36825T_TRIGGER_OWN_THREAD && CONFIG_VCNL36825T_TRIGGER && CONFIG_VCNL36825T && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/vishay/vcnl36825t/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl36825t/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VCNL36825T 接近传感器（Proximity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_VCNL36825T_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL36825T_TRIGGER_OWN_THREAD)、[`CONFIG_VCNL36825T_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VCNL36825T_TRIGGER)、[`CONFIG_VCNL36825T`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL36825T)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_VCNL36825T_TRIGGER`。

<a id="CONFIG_VCNL36825T_THREAD_STACK_SIZE"></a>

## 162.55 `CONFIG_VCNL36825T_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小（Thread Stack Size）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VCNL36825T_TRIGGER_OWN_THREAD && CONFIG_VCNL36825T_TRIGGER && CONFIG_VCNL36825T && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/vishay/vcnl36825t/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl36825t/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VCNL36825T 接近传感器（Proximity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_VCNL36825T_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL36825T_TRIGGER_OWN_THREAD)、[`CONFIG_VCNL36825T_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VCNL36825T_TRIGGER)、[`CONFIG_VCNL36825T`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL36825T)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_VCNL36825T_TRIGGER`。

<a id="CONFIG_VCNL36825T_TRIGGER_CHOICE"></a>

## 162.56 `CONFIG_VCNL36825T_TRIGGER_CHOICE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。原文注意事项指出，为判定触发的是哪一种中断，使用 Zephyr 标准类型时会禁用另一种中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_VCNL36825T && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_VCNL36825T_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_VCNL36825T_TRIGGER_NONE
CONFIG_VCNL36825T_TRIGGER_GLOBAL_THREAD
CONFIG_VCNL36825T_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/vishay/vcnl36825t/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl36825t/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VCNL36825T 接近传感器（Proximity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_VCNL36825T`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL36825T)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_VCNL36825T_TRIGGER_NONE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL36825T_TRIGGER_NONE)、[`CONFIG_VCNL36825T_TRIGGER_GLOBAL_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL36825T_TRIGGER_GLOBAL_THREAD)、[`CONFIG_VCNL36825T_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL36825T_TRIGGER_OWN_THREAD)。

<a id="CONFIG_VCNL36825T_TRIGGER_GLOBAL_THREAD"></a>

## 162.57 `CONFIG_VCNL36825T_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VCNL36825T_TRIGGER_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_VCNL36825T_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/vishay/vcnl36825t/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl36825t/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VCNL36825T 接近传感器（Proximity Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_VCNL36825T_TRIGGER_CHOICE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL36825T_TRIGGER_CHOICE)、[`CONFIG_VCNL36825T_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VCNL36825T_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_VCNL36825T_TRIGGER`。

<a id="CONFIG_VCNL36825T_TRIGGER_NONE"></a>

## 162.58 `CONFIG_VCNL36825T_TRIGGER_NONE`

**提示（Prompt）**：无触发器（No Trigger）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VCNL36825T_TRIGGER_CHOICE>
```

**定义位置（Location）**：[`drivers/sensor/vishay/vcnl36825t/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl36825t/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VCNL36825T 接近传感器（Proximity Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_VCNL36825T_TRIGGER_CHOICE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL36825T_TRIGGER_CHOICE)。

<a id="CONFIG_VCNL36825T_TRIGGER_OWN_THREAD"></a>

## 162.59 `CONFIG_VCNL36825T_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VCNL36825T_TRIGGER_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_VCNL36825T_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/vishay/vcnl36825t/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl36825t/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VCNL36825T 接近传感器（Proximity Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_VCNL36825T_TRIGGER_CHOICE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL36825T_TRIGGER_CHOICE)、[`CONFIG_VCNL36825T_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VCNL36825T_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_VCNL36825T_TRIGGER`。

<a id="CONFIG_VCNL4040"></a>

## 162.60 `CONFIG_VCNL4040`

**提示（Prompt）**：VCNL4040 接近与环境光传感器（Proximity and Ambient Light Sensor）

**说明（Help）**

启用 VCNL4040 传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VISHAY_VCNL4040_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/vishay/vcnl4040/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl4040/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_VCNL4040_ENABLE_ALS"></a>

## 162.61 `CONFIG_VCNL4040_ENABLE_ALS`

**提示（Prompt）**：环境光传感器（Ambient Light Sensor）

**说明（Help）**

启用环境光感应（ALS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_VCNL4040 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/vishay/vcnl4040/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl4040/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VCNL4040 接近与环境光传感器（Proximity and Ambient Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_VCNL4040`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL4040)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_VCNL4040_THREAD_PRIORITY"></a>

## 162.62 `CONFIG_VCNL4040_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VCNL4040_TRIGGER_OWN_THREAD && CONFIG_VCNL4040 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/vishay/vcnl4040/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl4040/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VCNL4040 接近与环境光传感器（Proximity and Ambient Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_VCNL4040_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL4040_TRIGGER_OWN_THREAD)、[`CONFIG_VCNL4040`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL4040)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_VCNL4040_THREAD_STACK_SIZE"></a>

## 162.63 `CONFIG_VCNL4040_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VCNL4040_TRIGGER_OWN_THREAD && CONFIG_VCNL4040 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/vishay/vcnl4040/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl4040/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VCNL4040 接近与环境光传感器（Proximity and Ambient Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_VCNL4040_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL4040_TRIGGER_OWN_THREAD)、[`CONFIG_VCNL4040`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL4040)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_VCNL4040_TRIGGER"></a>

## 162.64 `CONFIG_VCNL4040_TRIGGER`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_VCNL4040 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_VCNL4040_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_VCNL4040_TRIGGER_NONE
CONFIG_VCNL4040_TRIGGER_GLOBAL_THREAD
CONFIG_VCNL4040_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/vishay/vcnl4040/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl4040/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VCNL4040 接近与环境光传感器（Proximity and Ambient Light Sensor）

**配置项引用（Symbol References）**：[`CONFIG_VCNL4040`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL4040)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_VCNL4040_TRIGGER_NONE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL4040_TRIGGER_NONE)、[`CONFIG_VCNL4040_TRIGGER_GLOBAL_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL4040_TRIGGER_GLOBAL_THREAD)、[`CONFIG_VCNL4040_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL4040_TRIGGER_OWN_THREAD)。

<a id="CONFIG_VCNL4040_TRIGGER_GLOBAL_THREAD"></a>

## 162.65 `CONFIG_VCNL4040_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_VCNL4040_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/vishay/vcnl4040/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl4040/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VCNL4040 接近与环境光传感器（Proximity and Ambient Light Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_VCNL4040_TRIGGER`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL4040_TRIGGER)。

<a id="CONFIG_VCNL4040_TRIGGER_NONE"></a>

## 162.66 `CONFIG_VCNL4040_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VCNL4040_TRIGGER>
```

**定义位置（Location）**：[`drivers/sensor/vishay/vcnl4040/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl4040/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VCNL4040 接近与环境光传感器（Proximity and Ambient Light Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_VCNL4040_TRIGGER`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL4040_TRIGGER)。

<a id="CONFIG_VCNL4040_TRIGGER_OWN_THREAD"></a>

## 162.67 `CONFIG_VCNL4040_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_VCNL4040_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/vishay/vcnl4040/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl4040/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VCNL4040 接近与环境光传感器（Proximity and Ambient Light Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_VCNL4040_TRIGGER`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VCNL4040_TRIGGER)。

<a id="CONFIG_VEAA_X_3"></a>

## 162.68 `CONFIG_VEAA_X_3`

**提示（Prompt）**：VEAA-X-3 压力驱动（Pressure Driver）

**说明（Help）**

启用 Festo VEAA-X-3 驱动。驱动假定 ADC 最大值对应设备的最大输出值，DAC 最大值对应设备的最大输入值。ADC／DAC 与设备之间可能需要额外的外部硬件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FESTO_VEAA_X_3_ENABLED && CONFIG_ADC && CONFIG_DAC && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/veaa_x_3/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/veaa_x_3/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_DAC`](P072_drivers_dac_配置项参考.md#CONFIG_DAC)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_VEML6031"></a>

## 162.69 `CONFIG_VEML6031`

**提示（Prompt）**：Vishay VEML6031 环境光传感器（Ambient Light Sensor）

**说明（Help）**

启用 Vishay VEML6031 环境光传感器（Ambient Light Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VISHAY_VEML6031_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/vishay/veml6031/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/veml6031/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_VEML6046"></a>

## 162.70 `CONFIG_VEML6046`

**提示（Prompt）**：Vishay VEML6046 RGBIR 颜色传感器（Color Sensor）

**说明（Help）**

启用 Vishay VEML6046 RGBIR 颜色传感器（Color Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VISHAY_VEML6046_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/vishay/veml6046/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/veml6046/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_VEML7700"></a>

## 162.71 `CONFIG_VEML7700`

**提示（Prompt）**：Vishay VEML7700 环境光传感器（Ambient Light Sensor）

**说明（Help）**

启用 Vishay VEML7700 环境光传感器（Ambient Light Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VISHAY_VEML7700_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/vishay/veml7700/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/veml7700/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_VL53L0X"></a>

## 162.72 `CONFIG_VL53L0X`

**提示（Prompt）**：VL53L0X 飞行时间传感器（Time of Flight Sensor）

**说明（Help）**

启用基于 I2C 的 VL53L0X 飞行时间传感器（Time of Flight Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_VL53L0X_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO if n
CONFIG_HAS_STLIB
```

**定义位置（Location）**：[`drivers/sensor/st/vl53l0x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/vl53l0x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STLIB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STLIB`。

<a id="CONFIG_VL53L0X_PROXIMITY_THRESHOLD"></a>

## 162.73 `CONFIG_VL53L0X_PROXIMITY_THRESHOLD`

**提示（Prompt）**：接近检测阈值（Proximity Threshold），单位为毫米

**说明（Help）**

传感器使用 `SENSOR_CHAN_PROX` 时，用于接近检测（Proximity Detection）的阈值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VL53L0X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/sensor/st/vl53l0x/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/vl53l0x/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VL53L0X 飞行时间传感器（Time of Flight Sensor）

**配置项引用（Symbol References）**：[`CONFIG_VL53L0X`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VL53L0X)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_VL53L0X_RECONFIGURE_ADDRESS"></a>

## 162.74 `CONFIG_VL53L0X_RECONFIGURE_ADDRESS`

**提示（Prompt）**：支持重新配置传感器地址

**说明（Help）**

启用运行时重新配置传感器地址的支持。启用此选项后，设备树（Device Tree）中声明的所有传感器都必须具有 `xshut-gpio` 属性。初始化期间禁用所有传感器。首次从某个传感器读取数值时，驱动为其上电，并将其 I2C 地址从制造商默认值 `0x29` 重新配置为设备树中指定的地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_VL53L0X && CONFIG_SENSOR
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/x_nucleo_53l0a1/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_53l0a1/Kconfig.defconfig)。

```text
y if CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/vl53l0x/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/vl53l0x/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VL53L0X 飞行时间传感器（Time of Flight Sensor）

**配置项引用（Symbol References）**：[`CONFIG_VL53L0X`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VL53L0X)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_VL53L1X"></a>

## 162.75 `CONFIG_VL53L1X`

**提示（Prompt）**：VL53L1X 飞行时间传感器（Time of Flight Sensor）

**说明（Help）**

启用基于 I2C 的 VL53L1X 飞行时间传感器（Time of Flight Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_VL53L1X_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO if n || n
CONFIG_HAS_STLIB
```

**定义位置（Location）**：[`drivers/sensor/st/vl53l1x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/vl53l1x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STLIB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STLIB`。

<a id="CONFIG_VL53L1X_INTERRUPT_MODE"></a>

## 162.76 `CONFIG_VL53L1X_INTERRUPT_MODE`

**提示（Prompt）**：对 VL53L1X 飞行时间传感器使用中断模式（Interrupt Mode）

**说明（Help）**

启用 VL53L1X 飞行时间传感器的中断模式（Interrupt Mode）；否则，驱动使用轮询方式（Polling）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && CONFIG_VL53L1X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/vl53l1x/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/vl53l1x/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VL53L1X 飞行时间传感器（Time of Flight Sensor）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_VL53L1X`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VL53L1X)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_VL53L1X_XSHUT"></a>

## 162.77 `CONFIG_VL53L1X_XSHUT`

**提示（Prompt）**：使用 VL53L1X 飞行时间传感器的 xshut 引脚

**说明（Help）**

启用后使用 VL53L1X 的 `xshut` 引脚；否则，应将该引脚连接至 VDD。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && CONFIG_VL53L1X && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/vl53l1x/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/vl53l1x/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VL53L1X 飞行时间传感器（Time of Flight Sensor）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_VL53L1X`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VL53L1X)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_VL53L5CX"></a>

## 162.78 `CONFIG_VL53L5CX`

**提示（Prompt）**：VL53L5CX 飞行时间传感器（Time-of-Flight Sensor）

**说明（Help）**

启用 VL53L5CX 飞行时间传感器（Time-of-Flight Sensor）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_VL53L5CX_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_HAS_STLIB
CONFIG_RTIO_WORKQ if CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/st/vl53l5cx/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/vl53l5cx/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_HAS_STLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STLIB)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STLIB`。

<a id="CONFIG_VL53L5CX_MAX_I2C_CHUNK_SIZE"></a>

## 162.79 `CONFIG_VL53L5CX_MAX_I2C_CHUNK_SIZE`

**提示（Prompt）**：允许的最大 I2C 数据块（Chunk）大小

**说明（Help）**

允许限制每个 I2C 数据块（Chunk）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VL53L5CX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/vl53l5cx/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/vl53l5cx/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → VL53L5CX 飞行时间传感器（Time-of-Flight Sensor）

**配置项引用（Symbol References）**：[`CONFIG_VL53L5CX`](P162_drivers_sensor_配置项参考_14.md#CONFIG_VL53L5CX)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_VOLTAGE_DIVIDER"></a>

## 162.80 `CONFIG_VOLTAGE_DIVIDER`

**提示（Prompt）**：电压传感器（Voltage Sensor）驱动

**说明（Help）**

启用电压传感器（Voltage Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VOLTAGE_DIVIDER_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/sensor/voltage_divider/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/voltage_divider/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_WSEN_HIDS_2525020210002"></a>

## 162.81 `CONFIG_WSEN_HIDS_2525020210002`

**提示（Prompt）**：WSEN-HIDS-2525020210002 湿度传感器（Humidity Sensor）

**说明（Help）**

启用基于 I2C 的 WSEN-HIDS-2525020210002 湿度传感器（Humidity Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WE_WSEN_HIDS_2525020210002_ENABLED && CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_hids_2525020210002/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_hids_2525020210002/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_HAS_WESENSORS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_WESENSORS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE`、`CONFIG_HAS_WESENSORS`。

<a id="CONFIG_WSEN_ISDS_2536030320001"></a>

## 162.82 `CONFIG_WSEN_ISDS_2536030320001`

**提示（Prompt）**：WSEN-ISDS 三维加速度计与三维陀螺仪传感器

**说明（Help）**

启用基于 I2C/SPI 的 WSEN-ISDS 三维加速度计与三维陀螺仪传感器（3D Accelerometer and 3D Gyroscope Sensor）驱动，该器件集成温度传感器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WE_WSEN_ISDS_2536030320001_ENABLED && CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_HAS_WESENSORS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_WESENSORS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE`、`CONFIG_HAS_WESENSORS`。

<a id="CONFIG_WSEN_ISDS_2536030320001_DELTA"></a>

## 162.83 `CONFIG_WSEN_ISDS_2536030320001_DELTA`

**提示（Prompt）**：唤醒检测（Wake-up Detection，`SENSOR_TRIG_DELTA`）

**说明（Help）**

启用唤醒检测（Wake-up Detection，`SENSOR_TRIG_DELTA`）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_ISDS_2536030320001_TRIGGER && CONFIG_WSEN_ISDS_2536030320001 && CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_WSEN_ISDS_2536030320001_EVENTS
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ISDS 三维加速度计与三维陀螺仪传感器

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ISDS_2536030320001_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ISDS_2536030320001_TRIGGER)、[`CONFIG_WSEN_ISDS_2536030320001`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_WSEN_ISDS_2536030320001_EVENTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ISDS_2536030320001_EVENTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WSEN_ISDS_2536030320001_TRIGGER`、`CONFIG_WSEN_ISDS_2536030320001_EVENTS`。

<a id="CONFIG_WSEN_ISDS_2536030320001_DISABLE_ACCEL_HIGH_PERFORMANCE_MODE"></a>

## 162.84 `CONFIG_WSEN_ISDS_2536030320001_DISABLE_ACCEL_HIGH_PERFORMANCE_MODE`

**提示（Prompt）**：禁用加速度计高性能模式（High Performance Mode）

**说明（Help）**

禁用加速度计高性能模式（High Performance Mode）。禁用后，根据输出数据速率（ODR）在以下功耗模式间切换：

- 1.6 Hz 至 52 Hz：低功耗模式（Low Power Mode）。
- 104 Hz 至 208 Hz：正常功耗模式（Normal Power Mode）。
- 416 Hz 至 6.66 kHz：高性能模式（High Performance Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_ISDS_2536030320001 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ISDS 三维加速度计与三维陀螺仪传感器

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ISDS_2536030320001`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_WSEN_ISDS_2536030320001_DISABLE_GYRO_HIGH_PERFORMANCE_MODE"></a>

## 162.85 `CONFIG_WSEN_ISDS_2536030320001_DISABLE_GYRO_HIGH_PERFORMANCE_MODE`

**提示（Prompt）**：禁用陀螺仪高性能模式（High Performance Mode）

**说明（Help）**

禁用陀螺仪高性能模式（High Performance Mode）。禁用后，根据输出数据速率（ODR）在以下功耗模式间切换：

- 12.5 Hz 至 52 Hz：低功耗模式（Low Power Mode）。
- 104 Hz 至 208 Hz：正常功耗模式（Normal Power Mode）。
- 416 Hz 至 6.66 kHz：高性能模式（High Performance Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_ISDS_2536030320001 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ISDS 三维加速度计与三维陀螺仪传感器

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ISDS_2536030320001`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_WSEN_ISDS_2536030320001_FREEFALL"></a>

## 162.86 `CONFIG_WSEN_ISDS_2536030320001_FREEFALL`

**提示（Prompt）**：自由落体检测（Free-fall Detection）

**说明（Help）**

启用自由落体检测（Free-fall Detection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_ISDS_2536030320001_TRIGGER && CONFIG_WSEN_ISDS_2536030320001 && CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_WSEN_ISDS_2536030320001_EVENTS
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ISDS 三维加速度计与三维陀螺仪传感器

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ISDS_2536030320001_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ISDS_2536030320001_TRIGGER)、[`CONFIG_WSEN_ISDS_2536030320001`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_WSEN_ISDS_2536030320001_EVENTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ISDS_2536030320001_EVENTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WSEN_ISDS_2536030320001_TRIGGER`、`CONFIG_WSEN_ISDS_2536030320001_EVENTS`。

<a id="CONFIG_WSEN_ISDS_2536030320001_TAP"></a>

## 162.87 `CONFIG_WSEN_ISDS_2536030320001_TAP`

**提示（Prompt）**：单击与双击检测（Tap and Double Tap Detection）

**说明（Help）**

启用敲击检测（Tap Detection），包括单击和双击。注意，敲击识别推荐的输出数据速率（ODR）为 416 Hz 和 833 Hz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_ISDS_2536030320001_TRIGGER && CONFIG_WSEN_ISDS_2536030320001 && CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_WSEN_ISDS_2536030320001_EVENTS
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ISDS 三维加速度计与三维陀螺仪传感器

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ISDS_2536030320001_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ISDS_2536030320001_TRIGGER)、[`CONFIG_WSEN_ISDS_2536030320001`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_WSEN_ISDS_2536030320001_EVENTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ISDS_2536030320001_EVENTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WSEN_ISDS_2536030320001_TRIGGER`、`CONFIG_WSEN_ISDS_2536030320001_EVENTS`。

<a id="CONFIG_WSEN_ISDS_2536030320001_THREAD_PRIORITY"></a>

## 162.88 `CONFIG_WSEN_ISDS_2536030320001_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_ISDS_2536030320001_TRIGGER_OWN_THREAD && CONFIG_WSEN_ISDS_2536030320001 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ISDS 三维加速度计与三维陀螺仪传感器

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ISDS_2536030320001_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001_TRIGGER_OWN_THREAD)、[`CONFIG_WSEN_ISDS_2536030320001`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_WSEN_ISDS_2536030320001_THREAD_STACK_SIZE"></a>

## 162.89 `CONFIG_WSEN_ISDS_2536030320001_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_ISDS_2536030320001_TRIGGER_OWN_THREAD && CONFIG_WSEN_ISDS_2536030320001 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ISDS 三维加速度计与三维陀螺仪传感器

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ISDS_2536030320001_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001_TRIGGER_OWN_THREAD)、[`CONFIG_WSEN_ISDS_2536030320001`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_WSEN_ISDS_2536030320001_TRIGGER_GLOBAL_THREAD"></a>

## 162.90 `CONFIG_WSEN_ISDS_2536030320001_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_WSEN_ISDS_2536030320001_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_WSEN_ISDS_2536030320001_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ISDS 三维加速度计与三维陀螺仪传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_WSEN_ISDS_2536030320001_TRIGGER_MODE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001_TRIGGER_MODE)、[`CONFIG_WSEN_ISDS_2536030320001_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ISDS_2536030320001_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WSEN_ISDS_2536030320001_TRIGGER`。

<a id="CONFIG_WSEN_ISDS_2536030320001_TRIGGER_MODE"></a>

## 162.91 `CONFIG_WSEN_ISDS_2536030320001_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_ISDS_2536030320001 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_WSEN_ISDS_2536030320001_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_WSEN_ISDS_2536030320001_TRIGGER_NONE
CONFIG_WSEN_ISDS_2536030320001_TRIGGER_GLOBAL_THREAD
CONFIG_WSEN_ISDS_2536030320001_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ISDS 三维加速度计与三维陀螺仪传感器

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ISDS_2536030320001`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_WSEN_ISDS_2536030320001_TRIGGER_NONE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001_TRIGGER_NONE)、[`CONFIG_WSEN_ISDS_2536030320001_TRIGGER_GLOBAL_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001_TRIGGER_GLOBAL_THREAD)、[`CONFIG_WSEN_ISDS_2536030320001_TRIGGER_OWN_THREAD`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001_TRIGGER_OWN_THREAD)。

<a id="CONFIG_WSEN_ISDS_2536030320001_TRIGGER_NONE"></a>

## 162.92 `CONFIG_WSEN_ISDS_2536030320001_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WSEN_ISDS_2536030320001_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ISDS 三维加速度计与三维陀螺仪传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ISDS_2536030320001_TRIGGER_MODE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001_TRIGGER_MODE)。

<a id="CONFIG_WSEN_ISDS_2536030320001_TRIGGER_OWN_THREAD"></a>

## 162.93 `CONFIG_WSEN_ISDS_2536030320001_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_WSEN_ISDS_2536030320001_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_WSEN_ISDS_2536030320001_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_isds_2536030320001/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ISDS 三维加速度计与三维陀螺仪传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_WSEN_ISDS_2536030320001_TRIGGER_MODE`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ISDS_2536030320001_TRIGGER_MODE)、[`CONFIG_WSEN_ISDS_2536030320001_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ISDS_2536030320001_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WSEN_ISDS_2536030320001_TRIGGER`。

<a id="CONFIG_WSEN_ITDS_2533020201601"></a>

## 162.94 `CONFIG_WSEN_ITDS_2533020201601`

**提示（Prompt）**：WSEN-ITDS-2533020201601 三轴加速度传感器（3-axis Acceleration Sensor）

**说明（Help）**

启用基于 I2C/SPI、集成温度传感器的 WSEN-ITDS 加速度传感器（Acceleration Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WE_WSEN_ITDS_2533020201601_ENABLED && CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_HAS_WESENSORS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_WESENSORS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_WURTHELEKTRONIK_MODULE`、`CONFIG_HAS_WESENSORS`。

<a id="CONFIG_WSEN_ITDS_2533020201601_DELTA"></a>

## 162.95 `CONFIG_WSEN_ITDS_2533020201601_DELTA`

**提示（Prompt）**：唤醒检测（Wake-up Detection，`SENSOR_TRIG_DELTA`）

**说明（Help）**

启用唤醒检测（Wake-up Detection，`SENSOR_TRIG_DELTA`）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_ITDS_2533020201601_TRIGGER && CONFIG_WSEN_ITDS_2533020201601 && CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_WSEN_ITDS_2533020201601_EVENTS
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ITDS-2533020201601 三轴加速度传感器（3-axis Acceleration Sensor）

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ITDS_2533020201601_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ITDS_2533020201601_TRIGGER)、[`CONFIG_WSEN_ITDS_2533020201601`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ITDS_2533020201601)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_WSEN_ITDS_2533020201601_EVENTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ITDS_2533020201601_EVENTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WSEN_ITDS_2533020201601_TRIGGER`、`CONFIG_WSEN_ITDS_2533020201601_EVENTS`。

<a id="CONFIG_WSEN_ITDS_2533020201601_FREEFALL"></a>

## 162.96 `CONFIG_WSEN_ITDS_2533020201601_FREEFALL`

**提示（Prompt）**：自由落体检测（Free-fall Detection）

**说明（Help）**

启用自由落体检测（Free-fall Detection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_ITDS_2533020201601_TRIGGER && CONFIG_WSEN_ITDS_2533020201601 && CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_WSEN_ITDS_2533020201601_EVENTS
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ITDS-2533020201601 三轴加速度传感器（3-axis Acceleration Sensor）

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ITDS_2533020201601_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ITDS_2533020201601_TRIGGER)、[`CONFIG_WSEN_ITDS_2533020201601`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ITDS_2533020201601)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_WSEN_ITDS_2533020201601_EVENTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ITDS_2533020201601_EVENTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WSEN_ITDS_2533020201601_TRIGGER`、`CONFIG_WSEN_ITDS_2533020201601_EVENTS`。

<a id="CONFIG_WSEN_ITDS_2533020201601_TAP"></a>

## 162.97 `CONFIG_WSEN_ITDS_2533020201601_TAP`

**提示（Prompt）**：单击与双击检测（Tap and Double Tap Detection）

**说明（Help）**

启用敲击检测（Tap Detection），包括单击和双击。注意，使用敲击识别功能所需的最低输出数据速率（ODR）为 400 Hz。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_ITDS_2533020201601_TRIGGER && CONFIG_WSEN_ITDS_2533020201601 && CONFIG_SENSOR
```

**主动选择（Selects）**

```text
CONFIG_WSEN_ITDS_2533020201601_EVENTS
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ITDS-2533020201601 三轴加速度传感器（3-axis Acceleration Sensor）

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ITDS_2533020201601_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ITDS_2533020201601_TRIGGER)、[`CONFIG_WSEN_ITDS_2533020201601`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ITDS_2533020201601)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_WSEN_ITDS_2533020201601_EVENTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ITDS_2533020201601_EVENTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WSEN_ITDS_2533020201601_TRIGGER`、`CONFIG_WSEN_ITDS_2533020201601_EVENTS`。

<a id="CONFIG_WSEN_ITDS_2533020201601_THREAD_PRIORITY"></a>

## 162.98 `CONFIG_WSEN_ITDS_2533020201601_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_ITDS_2533020201601_TRIGGER_OWN_THREAD && CONFIG_WSEN_ITDS_2533020201601 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ITDS-2533020201601 三轴加速度传感器（3-axis Acceleration Sensor）

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ITDS_2533020201601_TRIGGER_OWN_THREAD`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_ITDS_2533020201601_TRIGGER_OWN_THREAD)、[`CONFIG_WSEN_ITDS_2533020201601`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ITDS_2533020201601)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_WSEN_ITDS_2533020201601_THREAD_STACK_SIZE"></a>

## 162.99 `CONFIG_WSEN_ITDS_2533020201601_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WSEN_ITDS_2533020201601_TRIGGER_OWN_THREAD && CONFIG_WSEN_ITDS_2533020201601 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ITDS-2533020201601 三轴加速度传感器（3-axis Acceleration Sensor）

**配置项引用（Symbol References）**：[`CONFIG_WSEN_ITDS_2533020201601_TRIGGER_OWN_THREAD`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_ITDS_2533020201601_TRIGGER_OWN_THREAD)、[`CONFIG_WSEN_ITDS_2533020201601`](P162_drivers_sensor_配置项参考_14.md#CONFIG_WSEN_ITDS_2533020201601)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)。

<a id="CONFIG_WSEN_ITDS_2533020201601_TRIGGER_GLOBAL_THREAD"></a>

## 162.100 `CONFIG_WSEN_ITDS_2533020201601_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

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

**定义位置（Location）**：[`drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/wsen/wsen_itds_2533020201601/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → WSEN-ITDS-2533020201601 三轴加速度传感器（3-axis Acceleration Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_WSEN_ITDS_2533020201601_TRIGGER_MODE`](P163_drivers_sensor_配置项参考_15.md#CONFIG_WSEN_ITDS_2533020201601_TRIGGER_MODE)、[`CONFIG_WSEN_ITDS_2533020201601_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WSEN_ITDS_2533020201601_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WSEN_ITDS_2533020201601_TRIGGER`。

<!-- kconfig-navigation -->

[上一章](P161_drivers_sensor_配置项参考_13.md) · [返回大纲](大纲.md) · [下一章](P163_drivers_sensor_配置项参考_15.md)
