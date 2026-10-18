---
id: learning.zephyr-docs.kconfig-reference.page-150
title: "`drivers/sensor`配置项参考（2/15）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第150章\_`drivers/sensor`配置项参考（2/15）

本章翻译官方 Kconfig 数据库中 `drivers/sensor` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ADXL372_INACTIVITY_THRESHOLD"></a>

## 150.1 `CONFIG_ADXL372_INACTIVITY_THRESHOLD`

**提示（Prompt）**：非活动阈值（Inactivity Threshold），单位为毫重力加速度（mg）

**说明（Help）**

非活动检测阈值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL372 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
400
```

**取值范围（Ranges）**

```text
[0, 200000]
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL372`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL372)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL372_INACTIVITY_TIME"></a>

## 150.2 `CONFIG_ADXL372_INACTIVITY_TIME`

**提示（Prompt）**：非活动时间（Inactivity Time）

**说明（Help）**

检测到非活动事件之前，所有启用轴必须持续低于非活动阈值的时间。此值表示加速度必须保持低于阈值的非活动定时器单位数量，原文以 26 ms 的倍数描述。ODR 为 3200 Hz 及以下时，每个编码单位为 26 ms；ODR 为 6400 Hz 时，每个编码单位为 13 ms。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL372 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL372`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL372)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL372_MEASUREMENT_MODE"></a>

## 150.3 `CONFIG_ADXL372_MEASUREMENT_MODE`

**提示（Prompt）**：测量模式（Measurement Mode）

**说明（Help）**

此模式下，按输出数据速率（Output Data Rate，ODR）持续提供加速度数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADXL372_OP_MODE>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计 → 工作模式（Operating Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADXL372_OP_MODE`](P150_drivers_sensor_配置项参考_2.md#CONFIG_ADXL372_OP_MODE)。

<a id="CONFIG_ADXL372_OP_MODE"></a>

## 150.4 `CONFIG_ADXL372_OP_MODE`

**提示（Prompt）**：工作模式（Operating Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL372 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_ADXL372_PEAK_DETECT_MODE
```

**可选项（Choices）**

```text
CONFIG_ADXL372_PEAK_DETECT_MODE
CONFIG_ADXL372_MEASUREMENT_MODE
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL372`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL372)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADXL372_PEAK_DETECT_MODE`](P150_drivers_sensor_配置项参考_2.md#CONFIG_ADXL372_PEAK_DETECT_MODE)、[`CONFIG_ADXL372_MEASUREMENT_MODE`](P150_drivers_sensor_配置项参考_2.md#CONFIG_ADXL372_MEASUREMENT_MODE)。

<a id="CONFIG_ADXL372_PEAK_DETECT_MODE"></a>

## 150.5 `CONFIG_ADXL372_PEAK_DETECT_MODE`

**提示（Prompt）**：最大峰值检测模式（Max Peak Detect Mode）

**说明（Help）**

在大多数高加速度（High-g）应用中，冲击事件峰值处的单个三轴加速度采样已包含足够的事件信息，无需完整加速度历史。此模式下，设备仅返回两次连续采样获取操作之间、超过阈值的峰值加速度（Peak Acceleration）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADXL372_OP_MODE>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计 → 工作模式（Operating Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADXL372_OP_MODE`](P150_drivers_sensor_配置项参考_2.md#CONFIG_ADXL372_OP_MODE)。

<a id="CONFIG_ADXL372_REFERENCED_ACTIVITY_DETECTION_MODE"></a>

## 150.6 `CONFIG_ADXL372_REFERENCED_ACTIVITY_DETECTION_MODE`

**提示（Prompt）**：使用参考式活动／非活动检测（Referenced Detection）

**说明（Help）**

活动检测可配置为参考式或绝对式。使用绝对式活动检测时，加速度采样值直接与用户设定的阈值比较，以判断是否存在运动。许多应用更适合依据相对参考点或参考方向的偏差进行活动检测，而非使用绝对阈值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL372 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL372`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL372)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ADXL372_STREAM"></a>

## 150.7 `CONFIG_ADXL372_STREAM`

**提示（Prompt）**：使用先进先出队列传输数据流（FIFO Streaming）

**说明（Help）**

使用此配置选项启用通过 RTIO 流式传输传感器数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RTIO && CONFIG_SENSOR_ASYNC_API && CONFIG_ADXL372 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADXL372_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_ADXL372`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL372)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADXL372_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL372_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL372_TRIGGER`。

<a id="CONFIG_ADXL372_THREAD_PRIORITY"></a>

## 150.8 `CONFIG_ADXL372_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL372_TRIGGER_OWN_THREAD && CONFIG_ADXL372_TRIGGER && CONFIG_ADXL372 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL372_TRIGGER_OWN_THREAD`](P150_drivers_sensor_配置项参考_2.md#CONFIG_ADXL372_TRIGGER_OWN_THREAD)、[`CONFIG_ADXL372_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL372_TRIGGER)、[`CONFIG_ADXL372`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL372)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL372_TRIGGER`。

<a id="CONFIG_ADXL372_THREAD_STACK_SIZE"></a>

## 150.9 `CONFIG_ADXL372_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL372_TRIGGER_OWN_THREAD && CONFIG_ADXL372_TRIGGER && CONFIG_ADXL372 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL372_TRIGGER_OWN_THREAD`](P150_drivers_sensor_配置项参考_2.md#CONFIG_ADXL372_TRIGGER_OWN_THREAD)、[`CONFIG_ADXL372_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL372_TRIGGER)、[`CONFIG_ADXL372`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL372)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL372_TRIGGER`。

<a id="CONFIG_ADXL372_TRIGGER_GLOBAL_THREAD"></a>

## 150.10 `CONFIG_ADXL372_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ADXL372_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADXL372_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL372_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL372_TRIGGER`。

<a id="CONFIG_ADXL372_TRIGGER_MODE"></a>

## 150.11 `CONFIG_ADXL372_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADXL372 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_ADXL372_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_ADXL372_TRIGGER_NONE
CONFIG_ADXL372_TRIGGER_GLOBAL_THREAD
CONFIG_ADXL372_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计

**配置项引用（Symbol References）**：[`CONFIG_ADXL372`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADXL372)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADXL372_TRIGGER_NONE`](P150_drivers_sensor_配置项参考_2.md#CONFIG_ADXL372_TRIGGER_NONE)、[`CONFIG_ADXL372_TRIGGER_GLOBAL_THREAD`](P150_drivers_sensor_配置项参考_2.md#CONFIG_ADXL372_TRIGGER_GLOBAL_THREAD)、[`CONFIG_ADXL372_TRIGGER_OWN_THREAD`](P150_drivers_sensor_配置项参考_2.md#CONFIG_ADXL372_TRIGGER_OWN_THREAD)。

<a id="CONFIG_ADXL372_TRIGGER_NONE"></a>

## 150.12 `CONFIG_ADXL372_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADXL372_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADXL372_TRIGGER_MODE`](P150_drivers_sensor_配置项参考_2.md#CONFIG_ADXL372_TRIGGER_MODE)。

<a id="CONFIG_ADXL372_TRIGGER_OWN_THREAD"></a>

## 150.13 `CONFIG_ADXL372_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ADXL372_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/adi/adxl372/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adxl372/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADXL372 三轴高加速度（High-g）I²C/SPI 加速度计 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ADXL372_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADXL372_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ADXL372_TRIGGER`。

<a id="CONFIG_AFBR_S50"></a>

## 150.14 `CONFIG_AFBR_S50`

**提示（Prompt）**：AFBR-S50 飞行时间（Time-of-Flight，ToF）传感器

**说明（Help）**

启用 AFBR-S50 飞行时间传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_AFBR_S50_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SENSOR_ASYNC_API
CONFIG_SPI
CONFIG_SPI_RTIO
CONFIG_RTIO_WORKQ
CONFIG_AFBR_LIB
CONFIG_PINCTRL
CONFIG_PINCTRL_NON_STATIC
```

**定义位置（Location）**：[`drivers/sensor/broadcom/afbr_s50/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/broadcom/afbr_s50/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_AFBR_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AFBR_LIB)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_PINCTRL_NON_STATIC`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL_NON_STATIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_AFBR_LIB`。

<a id="CONFIG_AGS10"></a>

## 150.15 `CONFIG_AGS10`

**提示（Prompt）**：AOSONG AGS10 总挥发性有机物（TVOC）传感器

**说明（Help）**

启用 AOSONG AGS10 TVOC 传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AOSONG_AGS10_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/aosong/ags10/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/aosong/ags10/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_AK8975"></a>

## 150.16 `CONFIG_AK8975`

**提示（Prompt）**：AK8975 磁力计（Magnetometer）

**说明（Help）**

启用 AK8975 磁力计驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ASAHI_KASEI_AK8975_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/asahi_kasei/ak8975/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/asahi_kasei/ak8975/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_AKM09918C"></a>

## 150.17 `CONFIG_AKM09918C`

**提示（Prompt）**：AKM09918C 磁力计

**说明（Help）**

启用 AK8975 磁力计驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ASAHI_KASEI_AKM09918C_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_I2C_RTIO if CONFIG_SENSOR_ASYNC_API
CONFIG_RTIO_WORKQ if CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/asahi_kasei/akm09918c/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/asahi_kasei/akm09918c/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)。

<a id="CONFIG_ALS31300"></a>

## 150.18 `CONFIG_ALS31300`

**提示（Prompt）**：ALS31300 三维线性霍尔效应传感器（3D Linear Hall-Effect Sensor）

**说明（Help）**

启用 ALS31300 三维线性霍尔效应传感器驱动。该传感器通过 I²C 接口提供 X、Y、Z 轴 12 位磁场测量值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ALLEGRO_ALS31300_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/als31300/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/als31300/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_AMD_SB_TSI"></a>

## 150.19 `CONFIG_AMD_SB_TSI`

**提示（Prompt）**：AMD SB 温度传感器接口（Temperature Sensor Interface）

**说明（Help）**

启用 SB 温度传感器接口驱动。这是 AMD SoC 上的 I²C 温度传感器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMD_SB_TSI_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/amd_sb_tsi/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/amd_sb_tsi/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_AMG88XX"></a>

## 150.20 `CONFIG_AMG88XX`

**提示（Prompt）**：AMG88XX 红外热电堆传感器（Infrared Thermopile Sensor）

**说明（Help）**

启用 AMG88XX 红外热电堆传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PANASONIC_AMG88XX_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/amg88xx/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/amg88xx/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_AMG88XX_THREAD_PRIORITY"></a>

## 150.21 `CONFIG_AMG88XX_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AMG88XX_TRIGGER_OWN_THREAD && CONFIG_AMG88XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/amg88xx/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/amg88xx/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → AMG88XX 红外热电堆传感器（Infrared Thermopile Sensor）

**配置项引用（Symbol References）**：[`CONFIG_AMG88XX_TRIGGER_OWN_THREAD`](P150_drivers_sensor_配置项参考_2.md#CONFIG_AMG88XX_TRIGGER_OWN_THREAD)、[`CONFIG_AMG88XX`](P150_drivers_sensor_配置项参考_2.md#CONFIG_AMG88XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_AMG88XX_THREAD_STACK_SIZE"></a>

## 150.22 `CONFIG_AMG88XX_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AMG88XX_TRIGGER_OWN_THREAD && CONFIG_AMG88XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/amg88xx/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/amg88xx/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → AMG88XX 红外热电堆传感器（Infrared Thermopile Sensor）

**配置项引用（Symbol References）**：[`CONFIG_AMG88XX_TRIGGER_OWN_THREAD`](P150_drivers_sensor_配置项参考_2.md#CONFIG_AMG88XX_TRIGGER_OWN_THREAD)、[`CONFIG_AMG88XX`](P150_drivers_sensor_配置项参考_2.md#CONFIG_AMG88XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_AMG88XX_TRIGGER_GLOBAL_THREAD"></a>

## 150.23 `CONFIG_AMG88XX_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_AMG88XX_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/amg88xx/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/amg88xx/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → AMG88XX 红外热电堆传感器（Infrared Thermopile Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_AMG88XX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMG88XX_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_AMG88XX_TRIGGER`。

<a id="CONFIG_AMG88XX_TRIGGER_NONE"></a>

## 150.24 `CONFIG_AMG88XX_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/amg88xx/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/amg88xx/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → AMG88XX 红外热电堆传感器（Infrared Thermopile Sensor） → 触发模式（Trigger Mode）

<a id="CONFIG_AMG88XX_TRIGGER_OWN_THREAD"></a>

## 150.25 `CONFIG_AMG88XX_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_AMG88XX_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/amg88xx/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/amg88xx/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → AMG88XX 红外热电堆传感器（Infrared Thermopile Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_AMG88XX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMG88XX_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_AMG88XX_TRIGGER`。

<a id="CONFIG_AMS_AS5048"></a>

## 150.26 `CONFIG_AMS_AS5048`

**提示（Prompt）**：AMS AS5048 磁性角度传感器（Magnetic Angle Sensor）

**说明（Help）**

启用 AMS AS5048 磁性旋转编码器（Magnetic Rotary Encoder）驱动，支持通过 SPI 接口读取绝对角度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMS_AS5048_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/sensor/ams/ams_as5048/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ams_as5048/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_AMS_AS5600"></a>

## 150.27 `CONFIG_AMS_AS5600`

**提示（Prompt）**：AS5600 角位置传感器（Angular Position Sensor）

**说明（Help）**

启用 AS5600 角位置传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMS_AS5600_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ams/ams_as5600/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ams_as5600/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_AMS_IAQ_CORE"></a>

## 150.28 `CONFIG_AMS_IAQ_CORE`

**提示（Prompt）**：iAQ-core 数字挥发性有机物（VOC）传感器

**说明（Help）**

启用 iAQ-core 数字 VOC 传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMS_IAQCORE_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ams/ams_iAQcore/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ams_iAQcore/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_APDS9253"></a>

## 150.29 `CONFIG_APDS9253`

**提示（Prompt）**：APDS9253 传感器

**说明（Help）**

启用 APDS9253 传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AVAGO_APDS9253_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/apds9253/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/apds9253/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_APDS9306"></a>

## 150.30 `CONFIG_APDS9306`

**提示（Prompt）**：APDS9306 传感器

**说明（Help）**

启用 APDS9306 数字光传感器（Digital Light Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AVAGO_APDS9306_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/apds9306/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/apds9306/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_APDS9960"></a>

## 150.31 `CONFIG_APDS9960`

**提示（Prompt）**：APDS9960 传感器

**说明（Help）**

启用 APDS9960 传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AVAGO_APDS9960_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/apds9960/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/apds9960/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_APDS9960_ENABLE_ALS"></a>

## 150.32 `CONFIG_APDS9960_ENABLE_ALS`

**提示（Prompt）**：环境光感应（Ambient Light Sense）

**说明（Help）**

启用环境光感应（ALS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_APDS9960 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/apds9960/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/apds9960/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → APDS9960 传感器

**配置项引用（Symbol References）**：[`CONFIG_APDS9960`](P150_drivers_sensor_配置项参考_2.md#CONFIG_APDS9960)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_APDS9960_ENABLE_GESTURE"></a>

## 150.33 `CONFIG_APDS9960_ENABLE_GESTURE`

**提示（Prompt）**：手势感应（Gesture Sense）

**说明（Help）**

启用手势感应。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_APDS9960 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/sensor/apds9960/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/apds9960/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → APDS9960 传感器

**配置项引用（Symbol References）**：[`CONFIG_APDS9960`](P150_drivers_sensor_配置项参考_2.md#CONFIG_APDS9960)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_APDS9960_FETCH_MODE"></a>

## 150.34 `CONFIG_APDS9960_FETCH_MODE`

**提示（Prompt）**：获取模式（Fetching Mode）

**说明（Help）**

指定是否等待中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_APDS9960 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_APDS9960_FETCH_MODE_INTERRUPT
```

**可选项（Choices）**

```text
CONFIG_APDS9960_FETCH_MODE_POLL
CONFIG_APDS9960_FETCH_MODE_INTERRUPT
```

**定义位置（Location）**：[`drivers/sensor/apds9960/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/apds9960/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → APDS9960 传感器

**配置项引用（Symbol References）**：[`CONFIG_APDS9960`](P150_drivers_sensor_配置项参考_2.md#CONFIG_APDS9960)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_APDS9960_FETCH_MODE_INTERRUPT`](P150_drivers_sensor_配置项参考_2.md#CONFIG_APDS9960_FETCH_MODE_INTERRUPT)、[`CONFIG_APDS9960_FETCH_MODE_POLL`](P150_drivers_sensor_配置项参考_2.md#CONFIG_APDS9960_FETCH_MODE_POLL)。

<a id="CONFIG_APDS9960_FETCH_MODE_INTERRUPT"></a>

## 150.35 `CONFIG_APDS9960_FETCH_MODE_INTERRUPT`

**提示（Prompt）**：等待中断（Wait for Interrupt）

**说明（Help）**

读取前等待中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/sensor/apds9960/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/apds9960/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → APDS9960 传感器 → 获取模式（Fetching Mode）

<a id="CONFIG_APDS9960_FETCH_MODE_POLL"></a>

## 150.36 `CONFIG_APDS9960_FETCH_MODE_POLL`

**提示（Prompt）**：无中断引脚轮询（Poll without Interrupt Pin）

**说明（Help）**

使用 I²C 检查采样。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_APDS9960_FETCH_MODE>
```

**定义位置（Location）**：[`drivers/sensor/apds9960/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/apds9960/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → APDS9960 传感器 → 获取模式（Fetching Mode）

**配置项引用（Symbol References）**：[`CONFIG_APDS9960_FETCH_MODE`](P150_drivers_sensor_配置项参考_2.md#CONFIG_APDS9960_FETCH_MODE)。

<a id="CONFIG_APDS9960_TRIGGER_GLOBAL_THREAD"></a>

## 150.37 `CONFIG_APDS9960_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_APDS9960_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/apds9960/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/apds9960/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → APDS9960 传感器 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_APDS9960_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_APDS9960_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_APDS9960_TRIGGER`。

<a id="CONFIG_APDS9960_TRIGGER_NONE"></a>

## 150.38 `CONFIG_APDS9960_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/apds9960/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/apds9960/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → APDS9960 传感器 → 触发模式（Trigger Mode）

<a id="CONFIG_BD8LB600FS_DIAGNOSTICS"></a>

## 150.39 `CONFIG_BD8LB600FS_DIAGNOSTICS`

**提示（Prompt）**：BD8LB600FS 的传感器

**说明（Help）**

启用低侧开关 BD8LB600FS 的开路负载检测（Open Load Detection）、过流保护（Over Current Protection）及过热关断（Thermal Shutdown）传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ROHM_BD8LB600FS_DIAGNOSTICS_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/sensor/rohm/bd8lb600fs/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/rohm/bd8lb600fs/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_BFLB_TSEN"></a>

## 150.40 `CONFIG_BFLB_TSEN`

**提示（Prompt）**：Bouffalo Lab 内部温度传感器（TSEN）

**说明（Help）**

启用 Bouffalo Lab SoC 内部芯片温度传感器（TSEN）驱动。TSEN 是内部 GPADC 输入，不使用外部引脚。驱动通过 BFLB ADC 驱动取得两个采样阶段的数据，通过切换 `TSVBE_LOW` 实现，并使用固定斜率及可用时从 eFuse 读取的校准偏移，将两者之差转换为摄氏温度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_TSEN_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/sensor/bflb/bflb_tsen/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bflb/bflb_tsen/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_BH1730"></a>

## 150.41 `CONFIG_BH1730`

**提示（Prompt）**：BH1730 环境光传感器（Ambient Light Sensor）

**说明（Help）**

启用 BH1730 环境光传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ROHM_BH1730_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/rohm/bh1730/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/rohm/bh1730/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_BH1750"></a>

## 150.42 `CONFIG_BH1750`

**提示（Prompt）**：BH1750 环境光传感器

**说明（Help）**

启用 BH1750 环境光传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ROHM_BH1750_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/rohm/bh1750/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/rohm/bh1750/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_BH1790"></a>

## 150.43 `CONFIG_BH1790`

**提示（Prompt）**：BH1790 心率监测 IC 用光学传感器（Optical Sensor）

**说明（Help）**

BH1790 心率监测 IC 用光学传感器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ROHM_BH1790_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/rohm/bh1790/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/rohm/bh1790/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_BMA280"></a>

## 150.44 `CONFIG_BMA280`

**提示（Prompt）**：BMA280 三轴加速度计系列

**说明（Help）**

启用 BMA280 基于 I²C 的三轴加速度传感器系列驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BOSCH_BMA280_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_BMA280_PMU_BW_1"></a>

## 150.45 `CONFIG_BMA280_PMU_BW_1`

**提示（Prompt）**：7.81 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列 → 加速度数据滤波器带宽（Filter Bandwidth）

<a id="CONFIG_BMA280_PMU_BW_2"></a>

## 150.46 `CONFIG_BMA280_PMU_BW_2`

**提示（Prompt）**：15.63 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列 → 加速度数据滤波器带宽（Filter Bandwidth）

<a id="CONFIG_BMA280_PMU_BW_3"></a>

## 150.47 `CONFIG_BMA280_PMU_BW_3`

**提示（Prompt）**：31.25 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列 → 加速度数据滤波器带宽（Filter Bandwidth）

<a id="CONFIG_BMA280_PMU_BW_4"></a>

## 150.48 `CONFIG_BMA280_PMU_BW_4`

**提示（Prompt）**：62.5 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列 → 加速度数据滤波器带宽（Filter Bandwidth）

<a id="CONFIG_BMA280_PMU_BW_5"></a>

## 150.49 `CONFIG_BMA280_PMU_BW_5`

**提示（Prompt）**：125 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列 → 加速度数据滤波器带宽（Filter Bandwidth）

<a id="CONFIG_BMA280_PMU_BW_6"></a>

## 150.50 `CONFIG_BMA280_PMU_BW_6`

**提示（Prompt）**：250 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列 → 加速度数据滤波器带宽（Filter Bandwidth）

<a id="CONFIG_BMA280_PMU_BW_7"></a>

## 150.51 `CONFIG_BMA280_PMU_BW_7`

**提示（Prompt）**：500 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列 → 加速度数据滤波器带宽（Filter Bandwidth）

<a id="CONFIG_BMA280_PMU_BW_8"></a>

## 150.52 `CONFIG_BMA280_PMU_BW_8`

**提示（Prompt）**：不滤波（Unfiltered）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列 → 加速度数据滤波器带宽（Filter Bandwidth）

<a id="CONFIG_BMA280_PMU_RANGE_16G"></a>

## 150.53 `CONFIG_BMA280_PMU_RANGE_16G`

**提示（Prompt）**：±16 g

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列 → 加速度测量量程（Measurement Range）

<a id="CONFIG_BMA280_PMU_RANGE_2G"></a>

## 150.54 `CONFIG_BMA280_PMU_RANGE_2G`

**提示（Prompt）**：±2 g

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列 → 加速度测量量程（Measurement Range）

<a id="CONFIG_BMA280_PMU_RANGE_4G"></a>

## 150.55 `CONFIG_BMA280_PMU_RANGE_4G`

**提示（Prompt）**：±4 g

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列 → 加速度测量量程（Measurement Range）

<a id="CONFIG_BMA280_PMU_RANGE_8G"></a>

## 150.56 `CONFIG_BMA280_PMU_RANGE_8G`

**提示（Prompt）**：±8 g

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列 → 加速度测量量程（Measurement Range）

<a id="CONFIG_BMA280_THREAD_PRIORITY"></a>

## 150.57 `CONFIG_BMA280_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMA280_TRIGGER_OWN_THREAD && CONFIG_BMA280 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列

**配置项引用（Symbol References）**：[`CONFIG_BMA280_TRIGGER_OWN_THREAD`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BMA280_TRIGGER_OWN_THREAD)、[`CONFIG_BMA280`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BMA280)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMA280_THREAD_STACK_SIZE"></a>

## 150.58 `CONFIG_BMA280_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMA280_TRIGGER_OWN_THREAD && CONFIG_BMA280 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列

**配置项引用（Symbol References）**：[`CONFIG_BMA280_TRIGGER_OWN_THREAD`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BMA280_TRIGGER_OWN_THREAD)、[`CONFIG_BMA280`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BMA280)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMA280_TRIGGER_GLOBAL_THREAD"></a>

## 150.59 `CONFIG_BMA280_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMA280_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMA280_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMA280_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMA280_TRIGGER`。

<a id="CONFIG_BMA280_TRIGGER_NONE"></a>

## 150.60 `CONFIG_BMA280_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列 → 触发模式（Trigger Mode）

<a id="CONFIG_BMA280_TRIGGER_OWN_THREAD"></a>

## 150.61 `CONFIG_BMA280_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMA280_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma280/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma280/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA280 三轴加速度计系列 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMA280_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMA280_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMA280_TRIGGER`。

<a id="CONFIG_BMA4XX"></a>

## 150.62 `CONFIG_BMA4XX`

**提示（Prompt）**：BMA4XX 三轴加速度传感器

**说明（Help）**

启用 Bosch BMA4XX 驱动，基于 I²C。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BOSCH_BMA4XX_ENABLED && CONFIG_SENSOR_ASYNC_API && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_I2C_RTIO
CONFIG_RTIO_WORKQ
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma4xx/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma4xx/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)。

<a id="CONFIG_BMA4XX_STREAM"></a>

## 150.63 `CONFIG_BMA4XX_STREAM`

**提示（Prompt）**：使用硬件先入先出队列（FIFO）流式传输数据

**说明（Help）**

使用此配置选项，启用通过实时 I/O（RTIO）子系统流式传输传感器数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma4xx/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma4xx/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA4XX 三轴加速度传感器

<a id="CONFIG_BMA4XX_TEMPERATURE"></a>

## 150.64 `CONFIG_BMA4XX_TEMPERATURE`

**提示（Prompt）**：允许读取 BMA4XX 芯片温度（Die Temperature）

**说明（Help）**

允许读取 BMA4XX 片上温度传感器。这会产生额外总线活动，并增加代码大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMA4XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma4xx/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma4xx/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA4XX 三轴加速度传感器

**配置项引用（Symbol References）**：[`CONFIG_BMA4XX`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BMA4XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMC150_MAGN"></a>

## 150.65 `CONFIG_BMC150_MAGN`

**提示（Prompt）**：BMC150_MAGN I²C 磁力计芯片

**说明（Help）**

启用 BMC150 基于 I²C 的磁力计传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BOSCH_BMC150_MAGN_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmc150_magn/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmc150_magn/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_BMC150_MAGN_PRESET_ENHANCED_REGULAR"></a>

## 150.66 `CONFIG_BMC150_MAGN_PRESET_ENHANCED_REGULAR`

**提示（Prompt）**：增强常规模式（Enhanced Regular），15、27、10

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmc150_magn/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmc150_magn/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMC150_MAGN I²C 磁力计芯片 → 属性（Attributes） → 默认预设（Default Preset）

<a id="CONFIG_BMC150_MAGN_PRESET_HIGH_ACCURACY"></a>

## 150.67 `CONFIG_BMC150_MAGN_PRESET_HIGH_ACCURACY`

**提示（Prompt）**：高精度（High Accuracy），47、83、20

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmc150_magn/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmc150_magn/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMC150_MAGN I²C 磁力计芯片 → 属性（Attributes） → 默认预设（Default Preset）

<a id="CONFIG_BMC150_MAGN_PRESET_LOW_POWER"></a>

## 150.68 `CONFIG_BMC150_MAGN_PRESET_LOW_POWER`

**提示（Prompt）**：低功耗（Low Power），3、3、10

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmc150_magn/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmc150_magn/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMC150_MAGN I²C 磁力计芯片 → 属性（Attributes） → 默认预设（Default Preset）

<a id="CONFIG_BMC150_MAGN_PRESET_REGULAR"></a>

## 150.69 `CONFIG_BMC150_MAGN_PRESET_REGULAR`

**提示（Prompt）**：常规模式（Regular），9、15、10

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmc150_magn/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmc150_magn/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMC150_MAGN I²C 磁力计芯片 → 属性（Attributes） → 默认预设（Default Preset）

<a id="CONFIG_BMC150_MAGN_SAMPLING_RATE_RUNTIME"></a>

## 150.70 `CONFIG_BMC150_MAGN_SAMPLING_RATE_RUNTIME`

**提示（Prompt）**：动态采样率（Dynamic Sampling Rate）

**说明（Help）**

启用在运行时修改采样率属性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMC150_MAGN && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmc150_magn/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmc150_magn/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMC150_MAGN I²C 磁力计芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_BMC150_MAGN`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BMC150_MAGN)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMC150_MAGN_SAMPLING_REP_XY"></a>

## 150.71 `CONFIG_BMC150_MAGN_SAMPLING_REP_XY`

**提示（Prompt）**：动态 XY 过采样（Dynamic XY Oversampling）

**说明（Help）**

启用在运行时修改 XY 过采样设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMC150_MAGN && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmc150_magn/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmc150_magn/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMC150_MAGN I²C 磁力计芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_BMC150_MAGN`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BMC150_MAGN)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMC150_MAGN_SAMPLING_REP_Z"></a>

## 150.72 `CONFIG_BMC150_MAGN_SAMPLING_REP_Z`

**提示（Prompt）**：动态 Z 过采样（Dynamic Z Oversampling）

**说明（Help）**

启用在运行时修改 Z 过采样设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMC150_MAGN && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmc150_magn/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmc150_magn/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMC150_MAGN I²C 磁力计芯片 → 属性（Attributes）

**配置项引用（Symbol References）**：[`CONFIG_BMC150_MAGN`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BMC150_MAGN)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMC150_MAGN_TRIGGER"></a>

## 150.73 `CONFIG_BMC150_MAGN_TRIGGER`

**提示（Prompt）**：触发器（Triggers）

**说明（Help）**

为 BMC150 磁力计启用触发器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmc150_magn/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmc150_magn/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMC150_MAGN I²C 磁力计芯片

<a id="CONFIG_BMC150_MAGN_TRIGGER_DRDY"></a>

## 150.74 `CONFIG_BMC150_MAGN_TRIGGER_DRDY`

**提示（Prompt）**：数据就绪触发（Data Ready Trigger）

**说明（Help）**

为 BMC150 磁力计启用数据就绪中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMC150_MAGN_TRIGGER && CONFIG_BMC150_MAGN && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmc150_magn/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmc150_magn/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMC150_MAGN I²C 磁力计芯片 → 触发器（Triggers）

**配置项引用（Symbol References）**：[`CONFIG_BMC150_MAGN_TRIGGER`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BMC150_MAGN_TRIGGER)、[`CONFIG_BMC150_MAGN`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BMC150_MAGN)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMC150_MAGN_TRIGGER_THREAD_STACK"></a>

## 150.75 `CONFIG_BMC150_MAGN_TRIGGER_THREAD_STACK`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

指定内部线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMC150_MAGN_TRIGGER && CONFIG_BMC150_MAGN && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmc150_magn/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmc150_magn/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMC150_MAGN I²C 磁力计芯片 → 触发器（Triggers）

**配置项引用（Symbol References）**：[`CONFIG_BMC150_MAGN_TRIGGER`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BMC150_MAGN_TRIGGER)、[`CONFIG_BMC150_MAGN`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BMC150_MAGN)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BME280"></a>

## 150.76 `CONFIG_BME280`

**提示（Prompt）**：BME280/BMP280 传感器

**说明（Help）**

启用 BME280 基于 I²C 或 SPI 的温度与压力传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BOSCH_BME280_ENABLED && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_BME280_FILTER_16"></a>

## 150.77 `CONFIG_BME280_FILTER_16`

**提示（Prompt）**：16

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 滤波器系数（Filter Coefficient）

<a id="CONFIG_BME280_FILTER_2"></a>

## 150.78 `CONFIG_BME280_FILTER_2`

**提示（Prompt）**：2

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 滤波器系数（Filter Coefficient）

<a id="CONFIG_BME280_FILTER_4"></a>

## 150.79 `CONFIG_BME280_FILTER_4`

**提示（Prompt）**：4

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 滤波器系数（Filter Coefficient）

<a id="CONFIG_BME280_FILTER_8"></a>

## 150.80 `CONFIG_BME280_FILTER_8`

**提示（Prompt）**：8

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 滤波器系数（Filter Coefficient）

<a id="CONFIG_BME280_FILTER_OFF"></a>

## 150.81 `CONFIG_BME280_FILTER_OFF`

**提示（Prompt）**：关闭滤波器（Filter Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 滤波器系数（Filter Coefficient）

<a id="CONFIG_BME280_HUMIDITY_OVER_16X"></a>

## 150.82 `CONFIG_BME280_HUMIDITY_OVER_16X`

**提示（Prompt）**：16 倍（x16）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 湿度过采样（Humidity Oversampling）

<a id="CONFIG_BME280_HUMIDITY_OVER_1X"></a>

## 150.83 `CONFIG_BME280_HUMIDITY_OVER_1X`

**提示（Prompt）**：1 倍（x1）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 湿度过采样（Humidity Oversampling）

<a id="CONFIG_BME280_HUMIDITY_OVER_2X"></a>

## 150.84 `CONFIG_BME280_HUMIDITY_OVER_2X`

**提示（Prompt）**：2 倍（x2）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 湿度过采样（Humidity Oversampling）

<a id="CONFIG_BME280_HUMIDITY_OVER_4X"></a>

## 150.85 `CONFIG_BME280_HUMIDITY_OVER_4X`

**提示（Prompt）**：4 倍（x4）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 湿度过采样（Humidity Oversampling）

<a id="CONFIG_BME280_HUMIDITY_OVER_8X"></a>

## 150.86 `CONFIG_BME280_HUMIDITY_OVER_8X`

**提示（Prompt）**：8 倍（x8）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 湿度过采样（Humidity Oversampling）

<a id="CONFIG_BME280_MODE"></a>

## 150.87 `CONFIG_BME280_MODE`

**提示（Prompt）**：BME280 采样模式（Sampling Mode）

**说明（Help）**

选择采样模式。正常模式（Normal Mode）执行连续测量，强制模式（Forced Mode）仅执行单次测量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BME280 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_BME280_MODE_NORMAL
```

**可选项（Choices）**

```text
CONFIG_BME280_MODE_NORMAL
CONFIG_BME280_MODE_FORCED
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器

**配置项引用（Symbol References）**：[`CONFIG_BME280`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BME280)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_BME280_MODE_NORMAL`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BME280_MODE_NORMAL)、[`CONFIG_BME280_MODE_FORCED`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BME280_MODE_FORCED)。

<a id="CONFIG_BME280_MODE_FORCED"></a>

## 150.88 `CONFIG_BME280_MODE_FORCED`

**提示（Prompt）**：强制（Forced）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BME280_MODE>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 采样模式（Sampling Mode）

**配置项引用（Symbol References）**：[`CONFIG_BME280_MODE`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BME280_MODE)。

<a id="CONFIG_BME280_MODE_NORMAL"></a>

## 150.89 `CONFIG_BME280_MODE_NORMAL`

**提示（Prompt）**：正常（Normal）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BME280_MODE>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 采样模式（Sampling Mode）

**配置项引用（Symbol References）**：[`CONFIG_BME280_MODE`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BME280_MODE)。

<a id="CONFIG_BME280_PRESS_OVER_16X"></a>

## 150.90 `CONFIG_BME280_PRESS_OVER_16X`

**提示（Prompt）**：16 倍（x16）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 压力过采样（Pressure Oversampling）

<a id="CONFIG_BME280_PRESS_OVER_1X"></a>

## 150.91 `CONFIG_BME280_PRESS_OVER_1X`

**提示（Prompt）**：1 倍（x1）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 压力过采样（Pressure Oversampling）

<a id="CONFIG_BME280_PRESS_OVER_2X"></a>

## 150.92 `CONFIG_BME280_PRESS_OVER_2X`

**提示（Prompt）**：2 倍（x2）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 压力过采样（Pressure Oversampling）

<a id="CONFIG_BME280_PRESS_OVER_4X"></a>

## 150.93 `CONFIG_BME280_PRESS_OVER_4X`

**提示（Prompt）**：4 倍（x4）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 压力过采样（Pressure Oversampling）

<a id="CONFIG_BME280_PRESS_OVER_8X"></a>

## 150.94 `CONFIG_BME280_PRESS_OVER_8X`

**提示（Prompt）**：8 倍（x8）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 压力过采样（Pressure Oversampling）

<a id="CONFIG_BME280_STANDBY_05MS"></a>

## 150.95 `CONFIG_BME280_STANDBY_05MS`

**提示（Prompt）**：0.5 ms

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 待机时间（Standby Time）

<a id="CONFIG_BME280_STANDBY_1000MS"></a>

## 150.96 `CONFIG_BME280_STANDBY_1000MS`

**提示（Prompt）**：1000 ms

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 待机时间（Standby Time）

<a id="CONFIG_BME280_STANDBY_125MS"></a>

## 150.97 `CONFIG_BME280_STANDBY_125MS`

**提示（Prompt）**：125 ms

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 待机时间（Standby Time）

<a id="CONFIG_BME280_STANDBY_2000MS"></a>

## 150.98 `CONFIG_BME280_STANDBY_2000MS`

**提示（Prompt）**：BMP280 为 2000 ms，BME280 为 10 ms

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 待机时间（Standby Time）

<a id="CONFIG_BME280_STANDBY_250MS"></a>

## 150.99 `CONFIG_BME280_STANDBY_250MS`

**提示（Prompt）**：250 ms

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 待机时间（Standby Time）

<a id="CONFIG_BME280_STANDBY_4000MS"></a>

## 150.100 `CONFIG_BME280_STANDBY_4000MS`

**提示（Prompt）**：BMP280 为 4000 ms，BME280 为 20 ms

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 待机时间（Standby Time）

<!-- kconfig-navigation -->

[上一章](P149_drivers_sensor_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P151_drivers_sensor_配置项参考_3.md)
