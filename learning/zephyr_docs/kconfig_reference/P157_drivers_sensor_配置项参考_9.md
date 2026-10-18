---
id: learning.zephyr-docs.kconfig-reference.page-157
title: "`drivers/sensor`配置项参考（9/15）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第157章\_`drivers/sensor`配置项参考（9/15）

本章翻译官方 Kconfig 数据库中 `drivers/sensor` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LM75_TRIGGER_NONE"></a>

## 157.1 `CONFIG_LM75_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/lm75/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/lm75/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LM75 温度传感器（Temperature Sensor） → 触发模式（Trigger Mode）

<a id="CONFIG_LM75_TRIGGER_THREAD_PRIO"></a>

## 157.2 `CONFIG_LM75_TRIGGER_THREAD_PRIO`

**提示（Prompt）**：触发工作队列线程（Trigger Workqueue Thread）的优先级

**说明（Help）**

内部触发工作队列线程的优先级等级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LM75_TRIGGER && CONFIG_LM75 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/sensor/lm75/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/lm75/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LM75 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_LM75_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LM75_TRIGGER)、[`CONFIG_LM75`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LM75)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LM75_TRIGGER`。

<a id="CONFIG_LM75_TRIGGER_THREAD_STACK_SIZE"></a>

## 157.3 `CONFIG_LM75_TRIGGER_THREAD_STACK_SIZE`

**提示（Prompt）**：触发工作队列线程（Trigger Workqueue Thread）的栈大小

**说明（Help）**

内部触发工作队列线程使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LM75_TRIGGER && CONFIG_LM75 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/sensor/lm75/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/lm75/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LM75 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_LM75_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LM75_TRIGGER)、[`CONFIG_LM75`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LM75)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LM75_TRIGGER`。

<a id="CONFIG_LM77"></a>

## 157.4 `CONFIG_LM77`

**提示（Prompt）**：LM77 温度传感器（Temperature Sensor）

**说明（Help）**

启用具有双线接口（2-wire Interface）的 LM77 数字温度传感器（Digital Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LM77_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
n
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/lm77/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/lm77/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_LM77_TRIGGER"></a>

## 157.5 `CONFIG_LM77_TRIGGER`

**提示（Prompt）**：触发支持（Trigger Support）

**说明（Help）**

启用 LM77 数字温度传感器的触发支持（Trigger Support）。触发事件基于 LM77 的 INT 信号，该信号配置为事件中断模式（Event Interrupt Mode）。发生触发事件后，必须读取 LM77 温度，以复位触发器并使其重新就绪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/lm77/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/lm77/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LM77 温度传感器（Temperature Sensor）

<a id="CONFIG_LM77_TRIGGER_THREAD_PRIO"></a>

## 157.6 `CONFIG_LM77_TRIGGER_THREAD_PRIO`

**提示（Prompt）**：触发工作队列线程（Trigger Workqueue Thread）的优先级

**说明（Help）**

内部触发工作队列线程的优先级等级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LM77_TRIGGER && CONFIG_LM77 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/sensor/lm77/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/lm77/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LM77 温度传感器（Temperature Sensor） → 触发支持（Trigger Support）

**配置项引用（Symbol References）**：[`CONFIG_LM77_TRIGGER`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LM77_TRIGGER)、[`CONFIG_LM77`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LM77)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LM77_TRIGGER_THREAD_STACK_SIZE"></a>

## 157.7 `CONFIG_LM77_TRIGGER_THREAD_STACK_SIZE`

**提示（Prompt）**：触发工作队列线程（Trigger Workqueue Thread）的栈大小

**说明（Help）**

内部触发工作队列线程使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LM77_TRIGGER && CONFIG_LM77 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/sensor/lm77/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/lm77/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LM77 温度传感器（Temperature Sensor） → 触发支持（Trigger Support）

**配置项引用（Symbol References）**：[`CONFIG_LM77_TRIGGER`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LM77_TRIGGER)、[`CONFIG_LM77`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LM77)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LM95234"></a>

## 157.8 `CONFIG_LM95234`

**提示（Prompt）**：LM95234 温度传感器（Temperature Sensor）

**说明（Help）**

启用具有系统管理总线（SMBus）接口的 LM95234 四路远程二极管与本地温度传感器（Quad Remote Diode and Local Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NATIONAL_LM95234_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/lm95234/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/lm95234/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_LPADC_TEMP40"></a>

## 157.9 `CONFIG_LPADC_TEMP40`

**提示（Prompt）**：NXP LPADC_TEMP40 温度传感器（Temperature Sensor）

**说明（Help）**

启用 NXP LPADC_TEMP40 温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPADC_TEMP40_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/sensor/nxp/nxp_lpadc_temp40/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/nxp_lpadc_temp40/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_LPS22HB"></a>

## 157.10 `CONFIG_LPS22HB`

**提示（Prompt）**：LPS22HB 压力与温度（Pressure and Temperature）

**说明（Help）**

启用基于 I2C 的 LPS22HB 压力与温度传感器（Pressure and Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LPS22HB_PRESS_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/st/lps22hb/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps22hb/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_LPS22HB_SAMPLING_RATE"></a>

## 157.11 `CONFIG_LPS22HB_SAMPLING_RATE`

**提示（Prompt）**：输出数据速率（Output Data Rate，ODR）

**说明（Help）**

传感器输出数据速率（Output Data Rate），以每秒采样数表示。芯片支持的数据速率为 1、10、25、50、75。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LPS22HB && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
25
```

**定义位置（Location）**：[`drivers/sensor/st/lps22hb/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps22hb/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LPS22HB 压力与温度（Pressure and Temperature）

**配置项引用（Symbol References）**：[`CONFIG_LPS22HB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS22HB)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LPS22HH"></a>

## 157.12 `CONFIG_LPS22HH`

**提示（Prompt）**：LPS22HH 压力与温度（Pressure and Temperature）

**说明（Help）**

启用基于 I2C 的 LPS22HH 压力与温度传感器（Pressure and Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LPS22HH_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_I3C if n
CONFIG_SPI if n
CONFIG_GPIO if n
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_LPS22HH
```

**定义位置（Location）**：[`drivers/sensor/st/lps22hh/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps22hh/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_LPS22HH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LPS22HH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_LPS22HH`。

<a id="CONFIG_LPS22HH_THREAD_PRIORITY"></a>

## 157.13 `CONFIG_LPS22HH_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LPS22HH_TRIGGER_OWN_THREAD && CONFIG_LPS22HH && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/lps22hh/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps22hh/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LPS22HH 压力与温度（Pressure and Temperature）

**配置项引用（Symbol References）**：[`CONFIG_LPS22HH_TRIGGER_OWN_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS22HH_TRIGGER_OWN_THREAD)、[`CONFIG_LPS22HH`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS22HH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LPS22HH_THREAD_STACK_SIZE"></a>

## 157.14 `CONFIG_LPS22HH_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LPS22HH_TRIGGER_OWN_THREAD && CONFIG_LPS22HH && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/lps22hh/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps22hh/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LPS22HH 压力与温度（Pressure and Temperature）

**配置项引用（Symbol References）**：[`CONFIG_LPS22HH_TRIGGER_OWN_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS22HH_TRIGGER_OWN_THREAD)、[`CONFIG_LPS22HH`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS22HH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LPS22HH_TRIGGER_GLOBAL_THREAD"></a>

## 157.15 `CONFIG_LPS22HH_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LPS22HH_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lps22hh/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps22hh/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LPS22HH 压力与温度（Pressure and Temperature） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LPS22HH_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LPS22HH_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LPS22HH_TRIGGER`。

<a id="CONFIG_LPS22HH_TRIGGER_MODE"></a>

## 157.16 `CONFIG_LPS22HH_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LPS22HH && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_LPS22HH_TRIGGER_GLOBAL_THREAD
```

**可选项（Choices）**

```text
CONFIG_LPS22HH_TRIGGER_NONE
CONFIG_LPS22HH_TRIGGER_GLOBAL_THREAD
CONFIG_LPS22HH_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/lps22hh/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps22hh/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LPS22HH 压力与温度（Pressure and Temperature）

**配置项引用（Symbol References）**：[`CONFIG_LPS22HH`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS22HH)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LPS22HH_TRIGGER_GLOBAL_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS22HH_TRIGGER_GLOBAL_THREAD)、[`CONFIG_LPS22HH_TRIGGER_NONE`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS22HH_TRIGGER_NONE)、[`CONFIG_LPS22HH_TRIGGER_OWN_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS22HH_TRIGGER_OWN_THREAD)。

<a id="CONFIG_LPS22HH_TRIGGER_NONE"></a>

## 157.17 `CONFIG_LPS22HH_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LPS22HH_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/lps22hh/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps22hh/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LPS22HH 压力与温度（Pressure and Temperature） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LPS22HH_TRIGGER_MODE`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS22HH_TRIGGER_MODE)。

<a id="CONFIG_LPS22HH_TRIGGER_OWN_THREAD"></a>

## 157.18 `CONFIG_LPS22HH_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LPS22HH_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lps22hh/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps22hh/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LPS22HH 压力与温度（Pressure and Temperature） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LPS22HH_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LPS22HH_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LPS22HH_TRIGGER`。

<a id="CONFIG_LPS25HB"></a>

## 157.19 `CONFIG_LPS25HB`

**提示（Prompt）**：LPS25HB 压力与温度（Pressure and Temperature）

**说明（Help）**

启用基于 I2C 的 LPS25HB 压力与温度传感器（Pressure and Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LPS25HB_PRESS_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/st/lps25hb/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps25hb/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_LPS25HB_SAMPLING_RATE"></a>

## 157.20 `CONFIG_LPS25HB_SAMPLING_RATE`

**提示（Prompt）**：输出数据速率（Output Data Rate，ODR）

**说明（Help）**

传感器输出数据速率（Output Data Rate），以每秒采样数表示。芯片支持的数据速率为 1、7、13、25。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LPS25HB && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
25
```

**定义位置（Location）**：[`drivers/sensor/st/lps25hb/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps25hb/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LPS25HB 压力与温度（Pressure and Temperature）

**配置项引用（Symbol References）**：[`CONFIG_LPS25HB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS25HB)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LPS2XDF"></a>

## 157.21 `CONFIG_LPS2XDF`

**提示（Prompt）**：LPS2xDF 压力与温度（Pressure and Temperature）

**说明（Help）**

启用基于 I2C 的 LPS2xDF 压力与温度传感器（Pressure and Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_LPS22DF_ENABLED || DT_HAS_ST_LPS28DFW_ENABLED || DT_HAS_ST_ILPS22QS_ENABLED) && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n || n || n
CONFIG_I3C if n || n || n
CONFIG_SPI if n || n
CONFIG_GPIO if n || n
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_ILPS22QS if DT_HAS_ST_ILPS22QS_ENABLED
CONFIG_USE_STDC_LPS22DF if DT_HAS_ST_LPS22DF_ENABLED
CONFIG_USE_STDC_LPS28DFW if DT_HAS_ST_LPS28DFW_ENABLED
```

**定义位置（Location）**：[`drivers/sensor/st/lps2xdf/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps2xdf/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_ILPS22QS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_ILPS22QS)、[`CONFIG_USE_STDC_LPS22DF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LPS22DF)、[`CONFIG_USE_STDC_LPS28DFW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LPS28DFW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_ILPS22QS`、`CONFIG_USE_STDC_LPS22DF`、`CONFIG_USE_STDC_LPS28DFW`。

<a id="CONFIG_LPS2XDF_THREAD_PRIORITY"></a>

## 157.22 `CONFIG_LPS2XDF_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LPS2XDF_TRIGGER_OWN_THREAD && CONFIG_LPS2XDF && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/lps2xdf/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps2xdf/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LPS2xDF 压力与温度（Pressure and Temperature）

**配置项引用（Symbol References）**：[`CONFIG_LPS2XDF_TRIGGER_OWN_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS2XDF_TRIGGER_OWN_THREAD)、[`CONFIG_LPS2XDF`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS2XDF)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LPS2XDF_THREAD_STACK_SIZE"></a>

## 157.23 `CONFIG_LPS2XDF_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LPS2XDF_TRIGGER_OWN_THREAD && CONFIG_LPS2XDF && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/lps2xdf/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps2xdf/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LPS2xDF 压力与温度（Pressure and Temperature）

**配置项引用（Symbol References）**：[`CONFIG_LPS2XDF_TRIGGER_OWN_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS2XDF_TRIGGER_OWN_THREAD)、[`CONFIG_LPS2XDF`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS2XDF)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LPS2XDF_TRIGGER_GLOBAL_THREAD"></a>

## 157.24 `CONFIG_LPS2XDF_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && (n || n) && <choice CONFIG_LPS2XDF_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_LPS2XDF_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lps2xdf/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps2xdf/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LPS2xDF 压力与温度（Pressure and Temperature） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_LPS2XDF_TRIGGER_MODE`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS2XDF_TRIGGER_MODE)、[`CONFIG_LPS2XDF_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LPS2XDF_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LPS2XDF_TRIGGER`。

<a id="CONFIG_LPS2XDF_TRIGGER_MODE"></a>

## 157.25 `CONFIG_LPS2XDF_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LPS2XDF && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_LPS2XDF_TRIGGER_GLOBAL_THREAD
```

**可选项（Choices）**

```text
CONFIG_LPS2XDF_TRIGGER_NONE
CONFIG_LPS2XDF_TRIGGER_GLOBAL_THREAD
CONFIG_LPS2XDF_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/lps2xdf/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps2xdf/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LPS2xDF 压力与温度（Pressure and Temperature）

**配置项引用（Symbol References）**：[`CONFIG_LPS2XDF`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS2XDF)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LPS2XDF_TRIGGER_GLOBAL_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS2XDF_TRIGGER_GLOBAL_THREAD)、[`CONFIG_LPS2XDF_TRIGGER_NONE`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS2XDF_TRIGGER_NONE)、[`CONFIG_LPS2XDF_TRIGGER_OWN_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS2XDF_TRIGGER_OWN_THREAD)。

<a id="CONFIG_LPS2XDF_TRIGGER_NONE"></a>

## 157.26 `CONFIG_LPS2XDF_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LPS2XDF_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/lps2xdf/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps2xdf/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LPS2xDF 压力与温度（Pressure and Temperature） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LPS2XDF_TRIGGER_MODE`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS2XDF_TRIGGER_MODE)。

<a id="CONFIG_LPS2XDF_TRIGGER_OWN_THREAD"></a>

## 157.27 `CONFIG_LPS2XDF_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_LPS2XDF_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_LPS2XDF_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lps2xdf/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lps2xdf/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LPS2xDF 压力与温度（Pressure and Temperature） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_LPS2XDF_TRIGGER_MODE`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LPS2XDF_TRIGGER_MODE)、[`CONFIG_LPS2XDF_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LPS2XDF_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LPS2XDF_TRIGGER`。

<a id="CONFIG_LSM303DLHC_MAGN"></a>

## 157.28 `CONFIG_LSM303DLHC_MAGN`

**提示（Prompt）**：LSM303DLHC 三轴磁力计（Three Axis Magnetometer）

**说明（Help）**

启用基于 I2C 的 LSM303DLHC 三轴磁力计传感器（Triaxial Magnetometer Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LSM303DLHC_MAGN_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/st/lsm303dlhc_magn/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm303dlhc_magn/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_LSM303DLHC_MAGN_ODR"></a>

## 157.29 `CONFIG_LSM303DLHC_MAGN_ODR`

**提示（Prompt）**：数据速率频率（Data Rate Frequency）

**说明（Help）**

数据速率对应关系：

- 0：0.75 Hz。
- 1：1.5 Hz。
- 2：3 Hz。
- 3：7.5 Hz。
- 4：15 Hz。
- 5：30 Hz。
- 6：75 Hz。
- 7：220 Hz。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM303DLHC_MAGN && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`drivers/sensor/st/lsm303dlhc_magn/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm303dlhc_magn/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM303DLHC 三轴磁力计（Three Axis Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_LSM303DLHC_MAGN`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM303DLHC_MAGN)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM303DLHC_MAGN_RANGE"></a>

## 157.30 `CONFIG_LSM303DLHC_MAGN_RANGE`

**提示（Prompt）**：磁力计测量范围（Magnetometer Measurement Range）

**说明（Help）**

测量范围对应关系：

- 1：±1.3 高斯（Gauss）。
- 2：±1.9 高斯。
- 3：±2.5 高斯。
- 4：±4 高斯。
- 5：±4.7 高斯。
- 6：±5.6 高斯。
- 7：±8.1 高斯。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM303DLHC_MAGN && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 7]
```

**定义位置（Location）**：[`drivers/sensor/st/lsm303dlhc_magn/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm303dlhc_magn/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM303DLHC 三轴磁力计（Three Axis Magnetometer）

**配置项引用（Symbol References）**：[`CONFIG_LSM303DLHC_MAGN`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM303DLHC_MAGN)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DS0"></a>

## 157.31 `CONFIG_LSM6DS0`

**提示（Prompt）**：LSM6DS0 I2C 加速度计与陀螺仪芯片

**说明（Help）**

启用基于 I2C 的 LSM6DS0 加速度计与陀螺仪传感器（Accelerometer and Gyroscope Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LSM6DS0_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6ds0/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6ds0/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_LSM6DS0_ACCEL_ENABLE_X_AXIS"></a>

## 157.32 `CONFIG_LSM6DS0_ACCEL_ENABLE_X_AXIS`

**提示（Prompt）**：加速度计 X 轴（Accelerometer X Axis）

**说明（Help）**

启用／禁用加速度计 X 轴；禁用时，从驱动中移除该轴的全部相关内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DS0 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6ds0/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6ds0/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DS0 I2C 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DS0`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DS0)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DS0_ACCEL_ENABLE_Y_AXIS"></a>

## 157.33 `CONFIG_LSM6DS0_ACCEL_ENABLE_Y_AXIS`

**提示（Prompt）**：加速度计 Y 轴（Accelerometer Y Axis）

**说明（Help）**

启用／禁用加速度计 Y 轴；禁用时，从驱动中移除该轴的全部相关内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DS0 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6ds0/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6ds0/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DS0 I2C 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DS0`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DS0)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DS0_ACCEL_ENABLE_Z_AXIS"></a>

## 157.34 `CONFIG_LSM6DS0_ACCEL_ENABLE_Z_AXIS`

**提示（Prompt）**：加速度计 Z 轴（Accelerometer Z Axis）

**说明（Help）**

启用／禁用加速度计 Z 轴；禁用时，从驱动中移除该轴的全部相关内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DS0 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6ds0/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6ds0/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DS0 I2C 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DS0`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DS0)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DS0_ACCEL_FULLSCALE"></a>

## 157.35 `CONFIG_LSM6DS0_ACCEL_FULLSCALE`

**提示（Prompt）**：加速度计满量程范围（Accelerometer Full-scale Range）

**说明（Help）**

指定默认加速度计满量程范围（Full-scale Range）。配置值 X 表示范围为 ±X G。有效值为 2、4、8 和 16。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DS0 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6ds0/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6ds0/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DS0 I2C 加速度计与陀螺仪芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DS0`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DS0)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DS0_ACCEL_SAMPLING_RATE"></a>

## 157.36 `CONFIG_LSM6DS0_ACCEL_SAMPLING_RATE`

**提示（Prompt）**：输出数据速率（Output Data Rate，ODR）

**说明（Help）**

指定默认加速度计输出数据速率（ODR），以每秒采样数（Hz）表示。芯片支持的数据速率为 0、10、50、119、238、476、952。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DS0 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6ds0/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6ds0/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DS0 I2C 加速度计与陀螺仪芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DS0`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DS0)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DS0_ENABLE_TEMP"></a>

## 157.37 `CONFIG_LSM6DS0_ENABLE_TEMP`

**提示（Prompt）**：温度（Temperature）

**说明（Help）**

启用／禁用温度功能；禁用时，从驱动中移除全部温度相关内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DS0 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6ds0/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6ds0/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DS0 I2C 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DS0`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DS0)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DS0_GYRO_ENABLE_X_AXIS"></a>

## 157.38 `CONFIG_LSM6DS0_GYRO_ENABLE_X_AXIS`

**提示（Prompt）**：陀螺仪 X 轴（Gyroscope X Axis）

**说明（Help）**

启用／禁用陀螺仪 X 轴；禁用时，从驱动中移除该轴的全部相关内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DS0 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6ds0/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6ds0/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DS0 I2C 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DS0`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DS0)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DS0_GYRO_ENABLE_Y_AXIS"></a>

## 157.39 `CONFIG_LSM6DS0_GYRO_ENABLE_Y_AXIS`

**提示（Prompt）**：陀螺仪 Y 轴（Gyroscope Y Axis）

**说明（Help）**

启用／禁用陀螺仪 Y 轴；禁用时，从驱动中移除该轴的全部相关内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DS0 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6ds0/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6ds0/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DS0 I2C 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DS0`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DS0)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DS0_GYRO_ENABLE_Z_AXIS"></a>

## 157.40 `CONFIG_LSM6DS0_GYRO_ENABLE_Z_AXIS`

**提示（Prompt）**：陀螺仪 Z 轴（Gyroscope Z Axis）

**说明（Help）**

启用／禁用陀螺仪 Z 轴；禁用时，从驱动中移除该轴的全部相关内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DS0 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6ds0/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6ds0/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DS0 I2C 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DS0`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DS0)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DS0_GYRO_FULLSCALE"></a>

## 157.41 `CONFIG_LSM6DS0_GYRO_FULLSCALE`

**提示（Prompt）**：陀螺仪满量程范围（Gyroscope Full-scale Range）

**说明（Help）**

指定默认陀螺仪满量程范围（Full-scale Range）。配置值 X 表示范围为 ±X 度／秒。有效值为 245、500 和 2000。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DS0 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
245
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6ds0/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6ds0/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DS0 I2C 加速度计与陀螺仪芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DS0`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DS0)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DS0_GYRO_SAMPLING_RATE"></a>

## 157.42 `CONFIG_LSM6DS0_GYRO_SAMPLING_RATE`

**提示（Prompt）**：输出数据速率（Output Data Rate，ODR）

**说明（Help）**

指定默认陀螺仪输出数据速率（ODR），以每秒采样数（Hz）表示。芯片支持的数据速率为 0、15、60、119、238、476、952。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DS0 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
15
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6ds0/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6ds0/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DS0 I2C 加速度计与陀螺仪芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DS0`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DS0)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSL"></a>

## 157.43 `CONFIG_LSM6DSL`

**提示（Prompt）**：LSM6DSL I2C/SPI 加速度计与陀螺仪芯片

**说明（Help）**

启用 LSM6DSL 加速度计与陀螺仪传感器（Accelerometer and Gyroscope Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LSM6DSL_ENABLED && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_LSM6DSL_ACCEL_FS"></a>

## 157.44 `CONFIG_LSM6DSL_ACCEL_FS`

**提示（Prompt）**：加速度计满量程范围（Accelerometer Full-scale Range）

**说明（Help）**

指定默认加速度计满量程范围（Full-scale Range）。配置值 X 表示范围为 ±X G。有效值为：

- 0：在运行时选择满量程。
- 2：±2 g。
- 4：±4 g。
- 8：±8 g。
- 16：±16 g。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSL_ACCEL_ODR"></a>

## 157.45 `CONFIG_LSM6DSL_ACCEL_ODR`

**提示（Prompt）**：加速度计输出数据速率（Accelerometer Output Data Rate）

**说明（Help）**

指定默认加速度计输出数据速率（ODR），以每秒采样数（Hz）表示。

- 0：在运行时选择 ODR。
- 1：12.5 Hz。
- 2：26 Hz。
- 3：52 Hz。
- 4：104 Hz。
- 5：208 Hz。
- 6：416 Hz。
- 7：833 Hz。
- 8：1666 Hz。
- 9：3332 Hz。
- 10：6664 Hz。
- 11：1.6 Hz。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 11]
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSL_ENABLE_TEMP"></a>

## 157.46 `CONFIG_LSM6DSL_ENABLE_TEMP`

**提示（Prompt）**：温度（Temperature）

**说明（Help）**

启用／禁用温度功能

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSL && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSL_EXT0_LIS2MDL"></a>

## 157.47 `CONFIG_LSM6DSL_EXT0_LIS2MDL`

**提示（Prompt）**：LIS2MDL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LSM6DSL_EXTERNAL_SENSOR_0>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能 → 外部传感器 0（External Sensor 0）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL_EXTERNAL_SENSOR_0`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL_EXTERNAL_SENSOR_0)。

<a id="CONFIG_LSM6DSL_EXT0_LIS3MDL"></a>

## 157.48 `CONFIG_LSM6DSL_EXT0_LIS3MDL`

**提示（Prompt）**：LIS3MDL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LSM6DSL_EXTERNAL_SENSOR_0>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能 → 外部传感器 0（External Sensor 0）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL_EXTERNAL_SENSOR_0`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL_EXTERNAL_SENSOR_0)。

<a id="CONFIG_LSM6DSL_EXT0_LPS22HB"></a>

## 157.49 `CONFIG_LSM6DSL_EXT0_LPS22HB`

**提示（Prompt）**：LPS22HB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LSM6DSL_EXTERNAL_SENSOR_0>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能 → 外部传感器 0（External Sensor 0）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL_EXTERNAL_SENSOR_0`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL_EXTERNAL_SENSOR_0)。

<a id="CONFIG_LSM6DSL_EXTERNAL_SENSOR_0"></a>

## 157.50 `CONFIG_LSM6DSL_EXTERNAL_SENSOR_0`

**提示（Prompt）**：外部传感器 0（External Sensor 0）

**说明（Help）**

选择连接到 LSM6DS3 的外部传感器 0（External Sensor 0）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSL_SENSORHUB && CONFIG_LSM6DSL && CONFIG_SENSOR
```

**可选项（Choices）**

```text
CONFIG_LSM6DSL_EXT0_LIS2MDL
CONFIG_LSM6DSL_EXT0_LIS3MDL
CONFIG_LSM6DSL_EXT0_LPS22HB
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL_SENSORHUB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL_SENSORHUB)、[`CONFIG_LSM6DSL`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LSM6DSL_EXT0_LIS2MDL`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL_EXT0_LIS2MDL)、[`CONFIG_LSM6DSL_EXT0_LIS3MDL`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL_EXT0_LIS3MDL)、[`CONFIG_LSM6DSL_EXT0_LPS22HB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL_EXT0_LPS22HB)。

<a id="CONFIG_LSM6DSL_GYRO_FS"></a>

## 157.51 `CONFIG_LSM6DSL_GYRO_FS`

**提示（Prompt）**：陀螺仪满量程范围（Gyroscope Full-scale Range）

**说明（Help）**

指定默认陀螺仪满量程范围（Full-scale Range）。配置值 X 表示范围为 ±X 度／秒。有效值为：

- 0：在运行时选择满量程。
- 125：±125 dps。
- 250：±250 dps。
- 500：±500 dps。
- 1000：±1000 dps。
- 2000：±2000 dps。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSL_GYRO_ODR"></a>

## 157.52 `CONFIG_LSM6DSL_GYRO_ODR`

**提示（Prompt）**：陀螺仪输出数据速率（Gyroscope Output Data Rate）

**说明（Help）**

原文说明为指定默认加速度计输出数据速率（ODR），以每秒采样数（Hz）表示。

- 0：在运行时选择 ODR。
- 1：12.5 Hz。
- 2：26 Hz。
- 3：52 Hz。
- 4：104 Hz。
- 5：208 Hz。
- 6：416 Hz。
- 7：833 Hz。
- 8：1660 Hz。
- 9：3330 Hz。
- 10：6660 Hz。

译注：该选项标题为陀螺仪（Gyroscope），帮助原文却写作加速度计（Accelerometer）；此处保留原文差异，未擅自更改速率数值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSL_SENSORHUB"></a>

## 157.53 `CONFIG_LSM6DSL_SENSORHUB`

**提示（Prompt）**：I2C 传感器集线器（Sensor Hub）功能

**说明（Help）**

启用／禁用内部传感器集线器（Sensor Hub）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSL && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSL_THREAD_PRIORITY"></a>

## 157.54 `CONFIG_LSM6DSL_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSL_TRIGGER_OWN_THREAD && CONFIG_LSM6DSL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL_TRIGGER_OWN_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL_TRIGGER_OWN_THREAD)、[`CONFIG_LSM6DSL`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSL_THREAD_STACK_SIZE"></a>

## 157.55 `CONFIG_LSM6DSL_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSL_TRIGGER_OWN_THREAD && CONFIG_LSM6DSL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL_TRIGGER_OWN_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL_TRIGGER_OWN_THREAD)、[`CONFIG_LSM6DSL`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSL_TRIGGER_GLOBAL_THREAD"></a>

## 157.56 `CONFIG_LSM6DSL_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LSM6DSL_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSL_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSL_TRIGGER`。

<a id="CONFIG_LSM6DSL_TRIGGER_MODE"></a>

## 157.57 `CONFIG_LSM6DSL_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSL && CONFIG_SENSOR
```

**可选项（Choices）**

```text
CONFIG_LSM6DSL_TRIGGER_NONE
CONFIG_LSM6DSL_TRIGGER_GLOBAL_THREAD
CONFIG_LSM6DSL_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LSM6DSL_TRIGGER_NONE`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL_TRIGGER_NONE)、[`CONFIG_LSM6DSL_TRIGGER_GLOBAL_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL_TRIGGER_GLOBAL_THREAD)、[`CONFIG_LSM6DSL_TRIGGER_OWN_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL_TRIGGER_OWN_THREAD)。

<a id="CONFIG_LSM6DSL_TRIGGER_NONE"></a>

## 157.58 `CONFIG_LSM6DSL_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LSM6DSL_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL_TRIGGER_MODE`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSL_TRIGGER_MODE)。

<a id="CONFIG_LSM6DSL_TRIGGER_OWN_THREAD"></a>

## 157.59 `CONFIG_LSM6DSL_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LSM6DSL_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsl/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsl/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSL I2C/SPI 加速度计与陀螺仪芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSL_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSL_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSL_TRIGGER`。

<a id="CONFIG_LSM6DSO"></a>

## 157.60 `CONFIG_LSM6DSO`

**提示（Prompt）**：LSM6DSO I2C/SPI 加速度计与陀螺仪芯片

**说明（Help）**

启用 LSM6DSO 加速度计与陀螺仪传感器（Accelerometer and Gyroscope Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_LSM6DSO_ENABLED || DT_HAS_ST_LSM6DSO32_ENABLED) && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n || n
CONFIG_SPI if n || n
CONFIG_GPIO if n || n
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_LSM6DSO
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_LSM6DSO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LSM6DSO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_LSM6DSO`。

<a id="CONFIG_LSM6DSO16IS"></a>

## 157.61 `CONFIG_LSM6DSO16IS`

**提示（Prompt）**：LSM6DSO16IS I2C/SPI 加速度计与陀螺仪芯片

**说明（Help）**

启用 LSM6DSO16IS 加速度计与陀螺仪传感器（Accelerometer and Gyroscope Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_LSM6DSO16IS_ENABLED && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
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
CONFIG_USE_STDC_LSM6DSO16IS
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso16is/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso16is/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_LSM6DSO16IS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LSM6DSO16IS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_LSM6DSO16IS`。

<a id="CONFIG_LSM6DSO16IS_ENABLE_TEMP"></a>

## 157.62 `CONFIG_LSM6DSO16IS_ENABLE_TEMP`

**提示（Prompt）**：温度（Temperature）

**说明（Help）**

启用／禁用温度功能

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO16IS && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso16is/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso16is/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO16IS I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO16IS`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSO16IS_EXT_HTS221"></a>

## 157.63 `CONFIG_LSM6DSO16IS_EXT_HTS221`

**提示（Prompt）**：将 HTS221 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO16IS_SENSORHUB && CONFIG_LSM6DSO16IS && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso16is/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso16is/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO16IS I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO16IS_SENSORHUB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS_SENSORHUB)、[`CONFIG_LSM6DSO16IS`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSO16IS_EXT_LIS2MDL"></a>

## 157.64 `CONFIG_LSM6DSO16IS_EXT_LIS2MDL`

**提示（Prompt）**：将 LIS2MDL 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO16IS_SENSORHUB && CONFIG_LSM6DSO16IS && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso16is/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso16is/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO16IS I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO16IS_SENSORHUB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS_SENSORHUB)、[`CONFIG_LSM6DSO16IS`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSO16IS_EXT_LPS22DF"></a>

## 157.65 `CONFIG_LSM6DSO16IS_EXT_LPS22DF`

**提示（Prompt）**：将 LPS22DF 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO16IS_SENSORHUB && CONFIG_LSM6DSO16IS && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso16is/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso16is/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO16IS I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO16IS_SENSORHUB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS_SENSORHUB)、[`CONFIG_LSM6DSO16IS`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSO16IS_EXT_LPS22HB"></a>

## 157.66 `CONFIG_LSM6DSO16IS_EXT_LPS22HB`

**提示（Prompt）**：将 LPS22HB 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO16IS_SENSORHUB && CONFIG_LSM6DSO16IS && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso16is/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso16is/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO16IS I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO16IS_SENSORHUB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS_SENSORHUB)、[`CONFIG_LSM6DSO16IS`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSO16IS_EXT_LPS22HH"></a>

## 157.67 `CONFIG_LSM6DSO16IS_EXT_LPS22HH`

**提示（Prompt）**：将 LPS22HH 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO16IS_SENSORHUB && CONFIG_LSM6DSO16IS && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso16is/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso16is/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO16IS I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO16IS_SENSORHUB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS_SENSORHUB)、[`CONFIG_LSM6DSO16IS`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSO16IS_SENSORHUB"></a>

## 157.68 `CONFIG_LSM6DSO16IS_SENSORHUB`

**提示（Prompt）**：I2C 传感器集线器（Sensor Hub）功能

**说明（Help）**

启用／禁用内部传感器集线器（Sensor Hub）。最多可启用两个外部传感器；如果启用了两个以上，系统只会枚举首先找到的两个。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO16IS && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso16is/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso16is/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO16IS I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO16IS`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSO16IS_THREAD_PRIORITY"></a>

## 157.69 `CONFIG_LSM6DSO16IS_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO16IS_TRIGGER_OWN_THREAD && CONFIG_LSM6DSO16IS_TRIGGER && CONFIG_LSM6DSO16IS && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso16is/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso16is/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO16IS I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO16IS_TRIGGER_OWN_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS_TRIGGER_OWN_THREAD)、[`CONFIG_LSM6DSO16IS_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSO16IS_TRIGGER)、[`CONFIG_LSM6DSO16IS`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSO16IS_TRIGGER`。

<a id="CONFIG_LSM6DSO16IS_THREAD_STACK_SIZE"></a>

## 157.70 `CONFIG_LSM6DSO16IS_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO16IS_TRIGGER_OWN_THREAD && CONFIG_LSM6DSO16IS_TRIGGER && CONFIG_LSM6DSO16IS && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso16is/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso16is/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO16IS I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO16IS_TRIGGER_OWN_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS_TRIGGER_OWN_THREAD)、[`CONFIG_LSM6DSO16IS_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSO16IS_TRIGGER)、[`CONFIG_LSM6DSO16IS`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSO16IS_TRIGGER`。

<a id="CONFIG_LSM6DSO16IS_TRIGGER_GLOBAL_THREAD"></a>

## 157.71 `CONFIG_LSM6DSO16IS_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LSM6DSO16IS_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso16is/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso16is/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO16IS I2C/SPI 加速度计与陀螺仪芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO16IS_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSO16IS_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSO16IS_TRIGGER`。

<a id="CONFIG_LSM6DSO16IS_TRIGGER_MODE"></a>

## 157.72 `CONFIG_LSM6DSO16IS_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO16IS && CONFIG_SENSOR
```

**可选项（Choices）**

```text
CONFIG_LSM6DSO16IS_TRIGGER_NONE
CONFIG_LSM6DSO16IS_TRIGGER_GLOBAL_THREAD
CONFIG_LSM6DSO16IS_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso16is/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso16is/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO16IS I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO16IS`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LSM6DSO16IS_TRIGGER_NONE`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS_TRIGGER_NONE)、[`CONFIG_LSM6DSO16IS_TRIGGER_GLOBAL_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS_TRIGGER_GLOBAL_THREAD)、[`CONFIG_LSM6DSO16IS_TRIGGER_OWN_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS_TRIGGER_OWN_THREAD)。

<a id="CONFIG_LSM6DSO16IS_TRIGGER_NONE"></a>

## 157.73 `CONFIG_LSM6DSO16IS_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LSM6DSO16IS_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso16is/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso16is/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO16IS I2C/SPI 加速度计与陀螺仪芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO16IS_TRIGGER_MODE`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO16IS_TRIGGER_MODE)。

<a id="CONFIG_LSM6DSO16IS_TRIGGER_OWN_THREAD"></a>

## 157.74 `CONFIG_LSM6DSO16IS_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LSM6DSO16IS_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso16is/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso16is/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO16IS I2C/SPI 加速度计与陀螺仪芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO16IS_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSO16IS_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSO16IS_TRIGGER`。

<a id="CONFIG_LSM6DSO_ENABLE_TEMP"></a>

## 157.75 `CONFIG_LSM6DSO_ENABLE_TEMP`

**提示（Prompt）**：温度（Temperature）

**说明（Help）**

启用／禁用温度功能

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSO_EXT_HTS221"></a>

## 157.76 `CONFIG_LSM6DSO_EXT_HTS221`

**提示（Prompt）**：将 HTS221 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO_SENSORHUB && CONFIG_LSM6DSO && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO_SENSORHUB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO_SENSORHUB)、[`CONFIG_LSM6DSO`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSO_EXT_LIS2MDL"></a>

## 157.77 `CONFIG_LSM6DSO_EXT_LIS2MDL`

**提示（Prompt）**：将 LIS2MDL 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO_SENSORHUB && CONFIG_LSM6DSO && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO_SENSORHUB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO_SENSORHUB)、[`CONFIG_LSM6DSO`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSO_EXT_LPS22HB"></a>

## 157.78 `CONFIG_LSM6DSO_EXT_LPS22HB`

**提示（Prompt）**：将 LPS22HB 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO_SENSORHUB && CONFIG_LSM6DSO && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO_SENSORHUB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO_SENSORHUB)、[`CONFIG_LSM6DSO`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSO_EXT_LPS22HH"></a>

## 157.79 `CONFIG_LSM6DSO_EXT_LPS22HH`

**提示（Prompt）**：将 LPS22HH 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO_SENSORHUB && CONFIG_LSM6DSO && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO_SENSORHUB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO_SENSORHUB)、[`CONFIG_LSM6DSO`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSO_SENSORHUB"></a>

## 157.80 `CONFIG_LSM6DSO_SENSORHUB`

**提示（Prompt）**：I2C 传感器集线器（Sensor Hub）功能

**说明（Help）**

启用／禁用内部传感器集线器（Sensor Hub）。最多可启用两个外部传感器；如果启用了两个以上，系统只会枚举首先找到的两个。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSO_TAP"></a>

## 157.81 `CONFIG_LSM6DSO_TAP`

**提示（Prompt）**：单击与双击检测（Tap and Tap-Tap Detection）

**说明（Help）**

启用敲击检测（Tap Detection），包括单击和双击。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO_TRIGGER && CONFIG_LSM6DSO && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSO_TRIGGER)、[`CONFIG_LSM6DSO`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSO_TRIGGER`。

<a id="CONFIG_LSM6DSO_THREAD_PRIORITY"></a>

## 157.82 `CONFIG_LSM6DSO_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO_TRIGGER_OWN_THREAD && CONFIG_LSM6DSO_TRIGGER && CONFIG_LSM6DSO && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO_TRIGGER_OWN_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO_TRIGGER_OWN_THREAD)、[`CONFIG_LSM6DSO_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSO_TRIGGER)、[`CONFIG_LSM6DSO`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSO_TRIGGER`。

<a id="CONFIG_LSM6DSO_THREAD_STACK_SIZE"></a>

## 157.83 `CONFIG_LSM6DSO_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO_TRIGGER_OWN_THREAD && CONFIG_LSM6DSO_TRIGGER && CONFIG_LSM6DSO && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO_TRIGGER_OWN_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO_TRIGGER_OWN_THREAD)、[`CONFIG_LSM6DSO_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSO_TRIGGER)、[`CONFIG_LSM6DSO`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSO_TRIGGER`。

<a id="CONFIG_LSM6DSO_TILT"></a>

## 157.84 `CONFIG_LSM6DSO_TILT`

**提示（Prompt）**：倾斜检测（Tilt Detection）

**说明（Help）**

启用倾斜检测（Tilt Detection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO_TRIGGER && CONFIG_LSM6DSO && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSO_TRIGGER)、[`CONFIG_LSM6DSO`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSO_TRIGGER`。

<a id="CONFIG_LSM6DSO_TRIGGER_GLOBAL_THREAD"></a>

## 157.85 `CONFIG_LSM6DSO_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LSM6DSO_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO I2C/SPI 加速度计与陀螺仪芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSO_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSO_TRIGGER`。

<a id="CONFIG_LSM6DSO_TRIGGER_MODE"></a>

## 157.86 `CONFIG_LSM6DSO_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSO && CONFIG_SENSOR
```

**可选项（Choices）**

```text
CONFIG_LSM6DSO_TRIGGER_NONE
CONFIG_LSM6DSO_TRIGGER_GLOBAL_THREAD
CONFIG_LSM6DSO_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LSM6DSO_TRIGGER_NONE`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO_TRIGGER_NONE)、[`CONFIG_LSM6DSO_TRIGGER_GLOBAL_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO_TRIGGER_GLOBAL_THREAD)、[`CONFIG_LSM6DSO_TRIGGER_OWN_THREAD`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO_TRIGGER_OWN_THREAD)。

<a id="CONFIG_LSM6DSO_TRIGGER_NONE"></a>

## 157.87 `CONFIG_LSM6DSO_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LSM6DSO_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO I2C/SPI 加速度计与陀螺仪芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSO_TRIGGER_MODE`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO_TRIGGER_MODE)。

<a id="CONFIG_LSM6DSO_TRIGGER_OWN_THREAD"></a>

## 157.88 `CONFIG_LSM6DSO_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_LSM6DSO_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_LSM6DSO_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dso/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSO I2C/SPI 加速度计与陀螺仪芯片 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_LSM6DSO_TRIGGER_MODE`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSO_TRIGGER_MODE)、[`CONFIG_LSM6DSO_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSO_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSO_TRIGGER`。

<a id="CONFIG_LSM6DSV16X"></a>

## 157.89 `CONFIG_LSM6DSV16X`

**提示（Prompt）**：LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片

**说明（Help）**

启用 LSM6DSV16X 加速度计与陀螺仪传感器（Accelerometer and Gyroscope Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_LSM6DSV16X_ENABLED || DT_HAS_ST_LSM6DSV32X_ENABLED) && CONFIG_ZEPHYR_HAL_ST_MODULE && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n || n
CONFIG_I3C if n || n
CONFIG_SPI if n || n
CONFIG_GPIO if n || n || n || n
CONFIG_I2C_RTIO if CONFIG_I2C && CONFIG_SENSOR_ASYNC_API
CONFIG_I3C_RTIO if CONFIG_I3C && CONFIG_SENSOR_ASYNC_API
CONFIG_SPI_RTIO if CONFIG_SPI && CONFIG_SENSOR_ASYNC_API
CONFIG_HAS_STMEMSC
CONFIG_USE_STDC_LSM6DSV16X
CONFIG_RTIO_WORKQ if CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ST_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ST_MODULE)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_I3C_RTIO`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_RTIO)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_HAS_STMEMSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STMEMSC)、[`CONFIG_USE_STDC_LSM6DSV16X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STDC_LSM6DSV16X)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ST_MODULE`、`CONFIG_HAS_STMEMSC`、`CONFIG_USE_STDC_LSM6DSV16X`。

<a id="CONFIG_LSM6DSV16X_ENABLE_TEMP"></a>

## 157.90 `CONFIG_LSM6DSV16X_ENABLE_TEMP`

**提示（Prompt）**：温度（Temperature）

**说明（Help）**

启用／禁用温度功能

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSV16X && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSV16X`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSV16X_EXT_HTS221"></a>

## 157.91 `CONFIG_LSM6DSV16X_EXT_HTS221`

**提示（Prompt）**：将 HTS221 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSV16X_SENSORHUB && CONFIG_LSM6DSV16X && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSV16X_SENSORHUB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X_SENSORHUB)、[`CONFIG_LSM6DSV16X`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSV16X_EXT_LIS2MDL"></a>

## 157.92 `CONFIG_LSM6DSV16X_EXT_LIS2MDL`

**提示（Prompt）**：将 LIS2MDL 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSV16X_SENSORHUB && CONFIG_LSM6DSV16X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSV16X_SENSORHUB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X_SENSORHUB)、[`CONFIG_LSM6DSV16X`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSV16X_EXT_LPS22DF"></a>

## 157.93 `CONFIG_LSM6DSV16X_EXT_LPS22DF`

**提示（Prompt）**：将 LPS22DF 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSV16X_SENSORHUB && CONFIG_LSM6DSV16X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSV16X_SENSORHUB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X_SENSORHUB)、[`CONFIG_LSM6DSV16X`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSV16X_EXT_LPS22HB"></a>

## 157.94 `CONFIG_LSM6DSV16X_EXT_LPS22HB`

**提示（Prompt）**：将 LPS22HB 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSV16X_SENSORHUB && CONFIG_LSM6DSV16X && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSV16X_SENSORHUB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X_SENSORHUB)、[`CONFIG_LSM6DSV16X`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSV16X_EXT_LPS22HH"></a>

## 157.95 `CONFIG_LSM6DSV16X_EXT_LPS22HH`

**提示（Prompt）**：将 LPS22HH 用作外部传感器（External Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSV16X_SENSORHUB && CONFIG_LSM6DSV16X && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片 → I2C 传感器集线器（Sensor Hub）功能

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSV16X_SENSORHUB`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X_SENSORHUB)、[`CONFIG_LSM6DSV16X`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSV16X_SELF_TEST"></a>

## 157.96 `CONFIG_LSM6DSV16X_SELF_TEST`

**提示（Prompt）**：自检属性（Self Test Attribute）

**说明（Help）**

启用对传感器自检位（Self Test Bits）的配置支持。适用的自检流程请参阅传感器数据手册。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSV16X && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSV16X`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSV16X_SENSORHUB"></a>

## 157.97 `CONFIG_LSM6DSV16X_SENSORHUB`

**提示（Prompt）**：I2C 传感器集线器（Sensor Hub）功能

**说明（Help）**

启用／禁用内部传感器集线器（Sensor Hub）。最多可启用两个外部传感器；如果启用了两个以上，系统只会枚举首先找到的两个。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSV16X && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSV16X`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_LSM6DSV16X_STREAM"></a>

## 157.98 `CONFIG_LSM6DSV16X_STREAM`

**提示（Prompt）**：使用硬件先入先出队列（FIFO）流式传输数据

**说明（Help）**

使用此配置选项，启用通过实时 I/O（RTIO）子系统流式传输传感器数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_I2C_RTIO || CONFIG_SPI_RTIO || CONFIG_I3C_RTIO) && CONFIG_SENSOR_ASYNC_API && CONFIG_LSM6DSV16X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_LSM6DSV16X_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_I3C_RTIO`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_LSM6DSV16X`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_LSM6DSV16X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSV16X_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSV16X_TRIGGER`。

<a id="CONFIG_LSM6DSV16X_THREAD_PRIORITY"></a>

## 157.99 `CONFIG_LSM6DSV16X_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSV16X_TRIGGER_OWN_THREAD && CONFIG_LSM6DSV16X_TRIGGER && CONFIG_LSM6DSV16X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSV16X_TRIGGER_OWN_THREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSV16X_TRIGGER_OWN_THREAD)、[`CONFIG_LSM6DSV16X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSV16X_TRIGGER)、[`CONFIG_LSM6DSV16X`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSV16X_TRIGGER`。

<a id="CONFIG_LSM6DSV16X_THREAD_STACK_SIZE"></a>

## 157.100 `CONFIG_LSM6DSV16X_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LSM6DSV16X_TRIGGER_OWN_THREAD && CONFIG_LSM6DSV16X_TRIGGER && CONFIG_LSM6DSV16X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/st/lsm6dsv16x/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dsv16x/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → LSM6DSV16X/LSM6DSV32X I3C/I2C/SPI 加速度计与陀螺仪芯片

**配置项引用（Symbol References）**：[`CONFIG_LSM6DSV16X_TRIGGER_OWN_THREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSV16X_TRIGGER_OWN_THREAD)、[`CONFIG_LSM6DSV16X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LSM6DSV16X_TRIGGER)、[`CONFIG_LSM6DSV16X`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LSM6DSV16X_TRIGGER`。

<!-- kconfig-navigation -->

[上一章](P156_drivers_sensor_配置项参考_8.md) · [返回大纲](大纲.md) · [下一章](P158_drivers_sensor_配置项参考_10.md)
