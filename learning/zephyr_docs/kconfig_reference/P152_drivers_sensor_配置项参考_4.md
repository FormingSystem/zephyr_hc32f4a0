---
id: learning.zephyr-docs.kconfig-reference.page-152
title: "`drivers/sensor`配置项参考（4/15）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第152章\_`drivers/sensor`配置项参考（4/15）

本章翻译官方 Kconfig 数据库中 `drivers/sensor` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BMI160_GYRO_ODR_50"></a>

## 152.1 `CONFIG_BMI160_GYRO_ODR_50`

**提示（Prompt）**：频率：50 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:196`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L196)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_GYRO_ODR_800"></a>

## 152.2 `CONFIG_BMI160_GYRO_ODR_800`

**提示（Prompt）**：频率：800 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:208`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L208)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_GYRO_ODR_RUNTIME"></a>

## 152.3 `CONFIG_BMI160_GYRO_ODR_RUNTIME`

**提示（Prompt）**：在运行时设置（Set at Runtime）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:190`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L190)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_GYRO_PMU_FAST_STARTUP"></a>

## 152.4 `CONFIG_BMI160_GYRO_PMU_FAST_STARTUP`

**提示（Prompt）**：快速启动（Fast Start-up）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪功耗模式（Gyroscope Power Mode）

<a id="CONFIG_BMI160_GYRO_PMU_NORMAL"></a>

## 152.5 `CONFIG_BMI160_GYRO_PMU_NORMAL`

**提示（Prompt）**：正常（Normal）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪功耗模式（Gyroscope Power Mode）

<a id="CONFIG_BMI160_GYRO_PMU_RUNTIME"></a>

## 152.6 `CONFIG_BMI160_GYRO_PMU_RUNTIME`

**提示（Prompt）**：在运行时设置（Set at Runtime）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪功耗模式（Gyroscope Power Mode）

<a id="CONFIG_BMI160_GYRO_PMU_SUSPEND"></a>

## 152.7 `CONFIG_BMI160_GYRO_PMU_SUSPEND`

**提示（Prompt）**：挂起／不使用（Suspended/Not Used）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪功耗模式（Gyroscope Power Mode）

<a id="CONFIG_BMI160_GYRO_RANGE_1000DPS"></a>

## 152.8 `CONFIG_BMI160_GYRO_RANGE_1000DPS`

**提示（Prompt）**：1000 度／秒（DPS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪量程设置（Range Setting）。

<a id="CONFIG_BMI160_GYRO_RANGE_125DPS"></a>

## 152.9 `CONFIG_BMI160_GYRO_RANGE_125DPS`

**提示（Prompt）**：125 度／秒（DPS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪量程设置（Range Setting）。

<a id="CONFIG_BMI160_GYRO_RANGE_2000DPS"></a>

## 152.10 `CONFIG_BMI160_GYRO_RANGE_2000DPS`

**提示（Prompt）**：2000 度／秒（DPS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪量程设置（Range Setting）。

<a id="CONFIG_BMI160_GYRO_RANGE_250DPS"></a>

## 152.11 `CONFIG_BMI160_GYRO_RANGE_250DPS`

**提示（Prompt）**：250 度／秒（DPS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪量程设置（Range Setting）。

<a id="CONFIG_BMI160_GYRO_RANGE_500DPS"></a>

## 152.12 `CONFIG_BMI160_GYRO_RANGE_500DPS`

**提示（Prompt）**：500 度／秒（DPS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪量程设置（Range Setting）。

<a id="CONFIG_BMI160_GYRO_RANGE_RUNTIME"></a>

## 152.13 `CONFIG_BMI160_GYRO_RANGE_RUNTIME`

**提示（Prompt）**：在运行时设置（Set at Runtime）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪量程设置（Range Setting）。

<a id="CONFIG_BMI160_THREAD_PRIORITY"></a>

## 152.14 `CONFIG_BMI160_THREAD_PRIORITY`

**提示（Prompt）**：专用线程优先级（Own Thread Priority）

**说明（Help）**

处理中断的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI160_TRIGGER_OWN_THREAD && CONFIG_BMI160 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU）

**配置项引用（Symbol References）**：[`CONFIG_BMI160_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI160_TRIGGER_OWN_THREAD)、[`CONFIG_BMI160`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI160)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI160_THREAD_STACK_SIZE"></a>

## 152.15 `CONFIG_BMI160_THREAD_STACK_SIZE`

**提示（Prompt）**：专用线程栈大小（Own Thread Stack Size）

**说明（Help）**

线程栈（Thread Stack）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI160_TRIGGER_OWN_THREAD && CONFIG_BMI160 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU）

**配置项引用（Symbol References）**：[`CONFIG_BMI160_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI160_TRIGGER_OWN_THREAD)、[`CONFIG_BMI160`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI160)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI160_TRIGGER_GLOBAL_THREAD"></a>

## 152.16 `CONFIG_BMI160_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMI160_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMI160_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMI160_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMI160_TRIGGER`。

<a id="CONFIG_BMI160_TRIGGER_NONE"></a>

## 152.17 `CONFIG_BMI160_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 触发模式（Trigger Mode）

<a id="CONFIG_BMI160_TRIGGER_OWN_THREAD"></a>

## 152.18 `CONFIG_BMI160_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMI160_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMI160_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMI160_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMI160_TRIGGER`。

<a id="CONFIG_BMI270"></a>

## 152.19 `CONFIG_BMI270`

**提示（Prompt）**：BMI270 惯性测量单元（Inertial Measurement Unit，IMU）

**说明（Help）**

启用基于 I2C 的 BMI270 惯性测量单元（IMU）传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BOSCH_BMI270_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_I2C_RTIO if n
CONFIG_SPI if n
CONFIG_SPI_RTIO if n
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)。

<a id="CONFIG_BMI270_FIFO_HEADERLESS"></a>

## 152.20 `CONFIG_BMI270_FIFO_HEADERLESS`

**提示（Prompt）**：使用 FIFO 无帧头模式（Headerless Mode，不含逐帧帧头）

**说明（Help）**

启用时，将 FIFO 配置为 `FIFO_CONFIG_1.fifo_header_en=0`。要求加速度计（Accelerometer）与陀螺仪（Gyroscope）的输出数据速率（ODR）相同。仅存储常规帧，不存储跳过帧、传感器时间帧或配置帧；水位值（Watermark）为 `WATERMARK_SAMPLES*12` 时，每次中断恰好对应指定数量的采样。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI270_STREAM && CONFIG_BMI270 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI270 惯性测量单元（Inertial Measurement Unit，IMU） → 通过 `sensor_stream()` 进行 FIFO 流式传输（Streaming）

**配置项引用（Symbol References）**：[`CONFIG_BMI270_STREAM`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270_STREAM)、[`CONFIG_BMI270`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI270_FIFO_ON_INT2"></a>

## 152.21 `CONFIG_BMI270_FIFO_ON_INT2`

**提示（Prompt）**：将 FIFO 水位／满中断路由至 INT2，而非 INT1

**说明（Help）**

默认将 FIFO 水位中断（Watermark Interrupt）与满中断（Full Interrupt）映射至 INT1，并将唯一的 `irq-gpios` 引脚分配给 INT1。仅当开发板将 FIFO 中断连接到传感器的 INT2 引脚时，才启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI270_STREAM && CONFIG_BMI270 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI270 惯性测量单元（Inertial Measurement Unit，IMU） → 通过 `sensor_stream()` 进行 FIFO 流式传输（Streaming）

**配置项引用（Symbol References）**：[`CONFIG_BMI270_STREAM`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270_STREAM)、[`CONFIG_BMI270`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI270_FIFO_POLL_FALLBACK"></a>

## 152.22 `CONFIG_BMI270_FIFO_POLL_FALLBACK`

**提示（Prompt）**：在 GPIO 中断之外增加基于轮询的 FIFO 后备机制（Polling Fallback）

**说明（Help）**

启用时，周期性地通过 SPI/I2C 轮询 FIFO 填充量，在达到水位值时触发读取，为没有连接 GPIO 中断线的硬件提供后备机制。轮询周期由 `BMI270_FIFO_POLL_PERIOD_MS` 设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI270_STREAM && CONFIG_BMI270 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI270 惯性测量单元（Inertial Measurement Unit，IMU） → 通过 `sensor_stream()` 进行 FIFO 流式传输（Streaming）

**配置项引用（Symbol References）**：[`CONFIG_BMI270_STREAM`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270_STREAM)、[`CONFIG_BMI270`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI270_FIFO_POLL_PERIOD_MS"></a>

## 152.23 `CONFIG_BMI270_FIFO_POLL_PERIOD_MS`

**提示（Prompt）**：FIFO 后备轮询周期（ms）

**说明（Help）**

后备轮询检查 FIFO 填充量的间隔，单位为毫秒。较小的值可降低延迟，但会增加 SPI/I2C 总线流量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI270_FIFO_POLL_FALLBACK && CONFIG_BMI270 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[10, 1000]
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI270 惯性测量单元（Inertial Measurement Unit，IMU） → 通过 `sensor_stream()` 进行 FIFO 流式传输（Streaming） → 在 GPIO 中断之外增加基于轮询的 FIFO 后备机制（Polling Fallback）

**配置项引用（Symbol References）**：[`CONFIG_BMI270_FIFO_POLL_FALLBACK`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270_FIFO_POLL_FALLBACK)、[`CONFIG_BMI270`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI270_FIFO_STREAM_BLOCK_SIZE"></a>

## 152.24 `CONFIG_BMI270_FIFO_STREAM_BLOCK_SIZE`

**提示（Prompt）**：流式传输 RTIO 内存池块大小（字节）

**说明（Help）**

必须与传感器数据流在 `RTIO_DEFINE_WITH_MEMPOOL` 中使用的内存块大小一致。每次 FIFO 读取量限制为一个内存块扣除编码帧头后的容量。所需大小为 `WATERMARK_SAMPLES*13 + CONTROL_MARGIN + ~32` 字节，其中约 32 字节用于编码帧头。默认值 384 在带帧头模式（Header Mode）下可容纳 10 个采样，计算为 `10*13+40+32=202`，并留有余量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI270_STREAM && CONFIG_BMI270 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
384
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI270 惯性测量单元（Inertial Measurement Unit，IMU） → 通过 `sensor_stream()` 进行 FIFO 流式传输（Streaming）

**配置项引用（Symbol References）**：[`CONFIG_BMI270_STREAM`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270_STREAM)、[`CONFIG_BMI270`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI270_FIFO_WATERMARK_CONTROL_MARGIN"></a>

## 152.25 `CONFIG_BMI270_FIFO_WATERMARK_CONTROL_MARGIN`

**提示（Prompt）**：为控制帧追加到 FIFO 字节水位值的字节数

**说明（Help）**

在带帧头模式（Header Mode）下，FIFO 可能在数据帧之间插入控制帧／跳过帧（Control/Skip Frame）。设置硬件水位寄存器时，将此余量加到 `WATERMARK_SAMPLES * frame_bytes` 上，使中断在至少收到 `WATERMARK_SAMPLES` 个数据帧后触发。如果不需要为控制帧留出额外空间，可设为 0。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI270_STREAM && !CONFIG_BMI270_FIFO_HEADERLESS && CONFIG_BMI270 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI270 惯性测量单元（Inertial Measurement Unit，IMU） → 通过 `sensor_stream()` 进行 FIFO 流式传输（Streaming）

**配置项引用（Symbol References）**：[`CONFIG_BMI270_STREAM`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270_STREAM)、[`CONFIG_BMI270_FIFO_HEADERLESS`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270_FIFO_HEADERLESS)、[`CONFIG_BMI270`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI270_FIFO_WATERMARK_SAMPLES"></a>

## 152.26 `CONFIG_BMI270_FIFO_WATERMARK_SAMPLES`

**提示（Prompt）**：以采样数表示的 FIFO 水位值（加速度计＋陀螺仪帧）

**说明（Help）**

每次水位中断期望取得的加速度计和陀螺仪数据采样数。在无帧头模式（Headerless Mode）下，字节水位值恰好为 `SAMPLES*12`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI270_STREAM && CONFIG_BMI270 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI270 惯性测量单元（Inertial Measurement Unit，IMU） → 通过 `sensor_stream()` 进行 FIFO 流式传输（Streaming）

**配置项引用（Symbol References）**：[`CONFIG_BMI270_STREAM`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270_STREAM)、[`CONFIG_BMI270`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI270_LOW_POWER_MODE"></a>

## 152.27 `CONFIG_BMI270_LOW_POWER_MODE`

**提示（Prompt）**：在所有输出数据速率（ODR）下强制使用低功耗（功耗优化）滤波模式

**说明（Help）**

启用时，无论输出数据速率（ODR）是多少，加速度计与陀螺仪始终使用功耗优化滤波模式，即 `acc_filter_perf=0`、`gyr_filter_perf=0`、`gyr_noise_perf=0`。默认情况下，驱动在 `ODR >= 100 Hz` 时切换到性能模式。启用此选项可节省功耗，但噪声会增大，因为不使用数字滤波／过采样率（OSR）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI270 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI270 惯性测量单元（Inertial Measurement Unit，IMU）

**配置项引用（Symbol References）**：[`CONFIG_BMI270`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI270_STREAM"></a>

## 152.28 `CONFIG_BMI270_STREAM`

**提示（Prompt）**：通过 `sensor_stream()` 进行 FIFO 流式传输（Streaming）

**说明（Help）**

使用标准 Zephyr `sensor_stream()` API 和 `SENSOR_TRIG_FIFO_WATERMARK` 触发器，启用 FIFO 水位／满事件的流式传输（Streaming）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI270 惯性测量单元（Inertial Measurement Unit，IMU）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_BMI270_THREAD_PRIORITY"></a>

## 152.29 `CONFIG_BMI270_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI270_TRIGGER_OWN_THREAD && CONFIG_BMI270 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI270 惯性测量单元（Inertial Measurement Unit，IMU）

**配置项引用（Symbol References）**：[`CONFIG_BMI270_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270_TRIGGER_OWN_THREAD)、[`CONFIG_BMI270`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI270_THREAD_STACK_SIZE"></a>

## 152.30 `CONFIG_BMI270_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI270_TRIGGER_OWN_THREAD && CONFIG_BMI270 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI270 惯性测量单元（Inertial Measurement Unit，IMU）

**配置项引用（Symbol References）**：[`CONFIG_BMI270_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270_TRIGGER_OWN_THREAD)、[`CONFIG_BMI270`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI270_TRIGGER_GLOBAL_THREAD"></a>

## 152.31 `CONFIG_BMI270_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMI270_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI270 惯性测量单元（Inertial Measurement Unit，IMU） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMI270_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMI270_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMI270_TRIGGER`。

<a id="CONFIG_BMI270_TRIGGER_MODE"></a>

## 152.32 `CONFIG_BMI270_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI270 && CONFIG_SENSOR
```

**可选项（Choices）**

```text
CONFIG_BMI270_TRIGGER_NONE
CONFIG_BMI270_TRIGGER_GLOBAL_THREAD
CONFIG_BMI270_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI270 惯性测量单元（Inertial Measurement Unit，IMU）

**配置项引用（Symbol References）**：[`CONFIG_BMI270`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_BMI270_TRIGGER_NONE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270_TRIGGER_NONE)、[`CONFIG_BMI270_TRIGGER_GLOBAL_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270_TRIGGER_GLOBAL_THREAD)、[`CONFIG_BMI270_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270_TRIGGER_OWN_THREAD)。

<a id="CONFIG_BMI270_TRIGGER_NONE"></a>

## 152.33 `CONFIG_BMI270_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BMI270_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI270 惯性测量单元（Inertial Measurement Unit，IMU） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMI270_TRIGGER_MODE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI270_TRIGGER_MODE)。

<a id="CONFIG_BMI270_TRIGGER_OWN_THREAD"></a>

## 152.34 `CONFIG_BMI270_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMI270_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi270/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi270/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI270 惯性测量单元（Inertial Measurement Unit，IMU） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMI270_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMI270_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMI270_TRIGGER`。

<a id="CONFIG_BMI323"></a>

## 152.35 `CONFIG_BMI323`

**提示（Prompt）**：BMI323 测量单元（Measurement Unit）

**说明（Help）**

启用 BMI323 惯性测量单元（IMU）传感器驱动。驱动实现以下功能：

- 分别启用和禁用加速度计与陀螺仪。
- 分别设置加速度计与陀螺仪的满量程（Full Scale）。
- 分别设置加速度计与陀螺仪的数据速率。
- 分别取得加速度计与陀螺仪的三轴（x、y、z）采样。
- 取得芯片裸片温度（Die Temperature）。
- 为加速度计数据就绪（Data Ready）和任意运动（Any Motion）设置触发器。

驱动实现设备电源管理（Device Power Management）和设备运行时电源管理（Device Runtime Power Management）。使用运行时电源管理时，初始化后进入挂起状态，通过软复位设备实现尽可能低的功耗；否则，在初始化时恢复设备。恢复时，初始化总线、启用特征引擎（Feature Engine），并初始化 INT1。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BOSCH_BMI323_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi323/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi323/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI323_BUS_I2C"></a>

## 152.36 `CONFIG_BMI323_BUS_I2C`

**提示（Prompt）**：BMI323 驱动的 I2C 总线支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_I2C_RTIO
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi323/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi323/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI323 测量单元（Measurement Unit）

**配置项引用（Symbol References）**：[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)。

<a id="CONFIG_BMI323_BUS_SPI"></a>

## 152.37 `CONFIG_BMI323_BUS_SPI`

**提示（Prompt）**：BMI323 驱动的 SPI 总线支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_SPI_RTIO
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi323/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi323/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI323 测量单元（Measurement Unit）

**配置项引用（Symbol References）**：[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)。

<a id="CONFIG_BMM150"></a>

## 152.38 `CONFIG_BMM150`

**提示（Prompt）**：BMM150 I2C 地磁芯片（Geomagnetic Chip）

**说明（Help）**

启用基于 I2C 的 BMM150 地磁传感器（Geomagnetic Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BOSCH_BMM150_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm150/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm150/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_BMM150_PRESET_ENHANCED_REGULAR"></a>

## 152.39 `CONFIG_BMM150_PRESET_ENHANCED_REGULAR`

**提示（Prompt）**：增强常规模式（Enhanced Regular），15、27、10

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm150/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm150/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM150 I2C 地磁芯片（Geomagnetic Chip） → 默认预设（Default Preset）

<a id="CONFIG_BMM150_PRESET_HIGH_ACCURACY"></a>

## 152.40 `CONFIG_BMM150_PRESET_HIGH_ACCURACY`

**提示（Prompt）**：高精度（High Accuracy），47、83、20

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm150/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm150/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM150 I2C 地磁芯片（Geomagnetic Chip） → 默认预设（Default Preset）

<a id="CONFIG_BMM150_PRESET_LOW_POWER"></a>

## 152.41 `CONFIG_BMM150_PRESET_LOW_POWER`

**提示（Prompt）**：低功耗（Low Power），3、3、10

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm150/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm150/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM150 I2C 地磁芯片（Geomagnetic Chip） → 默认预设（Default Preset）

<a id="CONFIG_BMM150_PRESET_REGULAR"></a>

## 152.42 `CONFIG_BMM150_PRESET_REGULAR`

**提示（Prompt）**：常规模式（Regular），9、15、10

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm150/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm150/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM150 I2C 地磁芯片（Geomagnetic Chip） → 默认预设（Default Preset）

<a id="CONFIG_BMM150_SAMPLING_RATE_RUNTIME"></a>

## 152.43 `CONFIG_BMM150_SAMPLING_RATE_RUNTIME`

**提示（Prompt）**：动态采样率（Dynamic Sampling Rate）

**说明（Help）**

启用在运行时修改采样率属性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMM150 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm150/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm150/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM150 I2C 地磁芯片（Geomagnetic Chip）

**配置项引用（Symbol References）**：[`CONFIG_BMM150`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM150)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMM150_SAMPLING_REP_XY"></a>

## 152.44 `CONFIG_BMM150_SAMPLING_REP_XY`

**提示（Prompt）**：动态 XY 过采样（Dynamic XY Oversampling）

**说明（Help）**

启用在运行时修改 XY 过采样设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMM150 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm150/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm150/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM150 I2C 地磁芯片（Geomagnetic Chip）

**配置项引用（Symbol References）**：[`CONFIG_BMM150`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM150)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMM150_SAMPLING_REP_Z"></a>

## 152.45 `CONFIG_BMM150_SAMPLING_REP_Z`

**提示（Prompt）**：动态 Z 过采样（Dynamic Z Oversampling）

**说明（Help）**

启用在运行时修改 Z 过采样设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMM150 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm150/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm150/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM150 I2C 地磁芯片（Geomagnetic Chip）

**配置项引用（Symbol References）**：[`CONFIG_BMM150`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM150)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMM150_THREAD_PRIORITY"></a>

## 152.46 `CONFIG_BMM150_THREAD_PRIORITY`

**提示（Prompt）**：专用线程优先级（Own Thread Priority）

**说明（Help）**

驱动用于处理中断的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMM150_TRIGGER_OWN_THREAD && CONFIG_BMM150 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm150/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm150/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM150 I2C 地磁芯片（Geomagnetic Chip）

**配置项引用（Symbol References）**：[`CONFIG_BMM150_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM150_TRIGGER_OWN_THREAD)、[`CONFIG_BMM150`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM150)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMM150_THREAD_STACK_SIZE"></a>

## 152.47 `CONFIG_BMM150_THREAD_STACK_SIZE`

**提示（Prompt）**：专用线程栈大小（Own Thread Stack Size）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMM150_TRIGGER_OWN_THREAD && CONFIG_BMM150 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm150/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm150/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM150 I2C 地磁芯片（Geomagnetic Chip）

**配置项引用（Symbol References）**：[`CONFIG_BMM150_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM150_TRIGGER_OWN_THREAD)、[`CONFIG_BMM150`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM150)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMM150_TRIGGER_DIRECT"></a>

## 152.48 `CONFIG_BMM150_TRIGGER_DIRECT`

**提示（Prompt）**：使用中断请求处理程序（IRQ Handler）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMM150_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm150/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm150/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM150 I2C 地磁芯片（Geomagnetic Chip） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMM150_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMM150_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMM150_TRIGGER`。

<a id="CONFIG_BMM150_TRIGGER_GLOBAL_THREAD"></a>

## 152.49 `CONFIG_BMM150_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMM150_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm150/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm150/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM150 I2C 地磁芯片（Geomagnetic Chip） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMM150_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMM150_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMM150_TRIGGER`。

<a id="CONFIG_BMM150_TRIGGER_MODE"></a>

## 152.50 `CONFIG_BMM150_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMM150 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_BMM150_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_BMM150_TRIGGER_NONE
CONFIG_BMM150_TRIGGER_GLOBAL_THREAD
CONFIG_BMM150_TRIGGER_OWN_THREAD
CONFIG_BMM150_TRIGGER_DIRECT
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm150/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm150/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM150 I2C 地磁芯片（Geomagnetic Chip）

**配置项引用（Symbol References）**：[`CONFIG_BMM150`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM150)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_BMM150_TRIGGER_NONE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM150_TRIGGER_NONE)、[`CONFIG_BMM150_TRIGGER_GLOBAL_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM150_TRIGGER_GLOBAL_THREAD)、[`CONFIG_BMM150_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM150_TRIGGER_OWN_THREAD)、[`CONFIG_BMM150_TRIGGER_DIRECT`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM150_TRIGGER_DIRECT)。

<a id="CONFIG_BMM150_TRIGGER_NONE"></a>

## 152.51 `CONFIG_BMM150_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BMM150_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm150/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm150/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM150 I2C 地磁芯片（Geomagnetic Chip） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMM150_TRIGGER_MODE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM150_TRIGGER_MODE)。

<a id="CONFIG_BMM150_TRIGGER_OWN_THREAD"></a>

## 152.52 `CONFIG_BMM150_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMM150_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm150/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm150/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM150 I2C 地磁芯片（Geomagnetic Chip） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMM150_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMM150_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMM150_TRIGGER`。

<a id="CONFIG_BMM350"></a>

## 152.53 `CONFIG_BMM350`

**提示（Prompt）**：BMM350 地磁芯片（Geomagnetic Chip）

**说明（Help）**

启用基于 I2C/I3C 的 BMM350 地磁传感器（Geomagnetic Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BOSCH_BMM350_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_I2C_RTIO if n
CONFIG_I3C if n
CONFIG_I3C_RTIO if n
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm350/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm350/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_RTIO`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_RTIO)。

<a id="CONFIG_BMM350_STREAM"></a>

## 152.54 `CONFIG_BMM350_STREAM`

**提示（Prompt）**：流式模式（Streaming Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm350/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm350/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM350 地磁芯片（Geomagnetic Chip）

<a id="CONFIG_BMM350_THREAD_PRIORITY"></a>

## 152.55 `CONFIG_BMM350_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMM350_TRIGGER_OWN_THREAD && CONFIG_BMM350_TRIGGER && CONFIG_BMM350 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM350 地磁芯片（Geomagnetic Chip）

**配置项引用（Symbol References）**：[`CONFIG_BMM350_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM350_TRIGGER_OWN_THREAD)、[`CONFIG_BMM350_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMM350_TRIGGER)、[`CONFIG_BMM350`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM350)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMM350_TRIGGER`。

<a id="CONFIG_BMM350_THREAD_STACK_SIZE"></a>

## 152.56 `CONFIG_BMM350_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMM350_TRIGGER_OWN_THREAD && CONFIG_BMM350_TRIGGER && CONFIG_BMM350 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM350 地磁芯片（Geomagnetic Chip）

**配置项引用（Symbol References）**：[`CONFIG_BMM350_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM350_TRIGGER_OWN_THREAD)、[`CONFIG_BMM350_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMM350_TRIGGER)、[`CONFIG_BMM350`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM350)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMM350_TRIGGER`。

<a id="CONFIG_BMM350_TRIGGER_GLOBAL_THREAD"></a>

## 152.57 `CONFIG_BMM350_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_BMM350_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_BMM350_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM350 地磁芯片（Geomagnetic Chip） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_BMM350_TRIGGER_MODE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM350_TRIGGER_MODE)、[`CONFIG_BMM350_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMM350_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMM350_TRIGGER`。

<a id="CONFIG_BMM350_TRIGGER_MODE"></a>

## 152.58 `CONFIG_BMM350_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定传感器模块使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMM350 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_BMM350_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_BMM350_TRIGGER_NONE
CONFIG_BMM350_TRIGGER_GLOBAL_THREAD
CONFIG_BMM350_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM350 地磁芯片（Geomagnetic Chip）

**配置项引用（Symbol References）**：[`CONFIG_BMM350`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM350)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_BMM350_TRIGGER_NONE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM350_TRIGGER_NONE)、[`CONFIG_BMM350_TRIGGER_GLOBAL_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM350_TRIGGER_GLOBAL_THREAD)、[`CONFIG_BMM350_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM350_TRIGGER_OWN_THREAD)。

<a id="CONFIG_BMM350_TRIGGER_NONE"></a>

## 152.59 `CONFIG_BMM350_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BMM350_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM350 地磁芯片（Geomagnetic Chip） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMM350_TRIGGER_MODE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM350_TRIGGER_MODE)。

<a id="CONFIG_BMM350_TRIGGER_OWN_THREAD"></a>

## 152.60 `CONFIG_BMM350_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && <choice CONFIG_BMM350_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_BMM350_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/Kconfig.trigger_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/Kconfig.trigger_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM350 地磁芯片（Geomagnetic Chip） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_BMM350_TRIGGER_MODE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM350_TRIGGER_MODE)、[`CONFIG_BMM350_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMM350_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMM350_TRIGGER`。

<a id="CONFIG_BMP180"></a>

## 152.61 `CONFIG_BMP180`

**提示（Prompt）**：Bosch BMP180 压力传感器（Pressure Sensor）

**说明（Help）**

启用 Bosch BMP180 压力传感器（Pressure Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BOSCH_BMP180_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmp180/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp180/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_BMP180_OSR_RUNTIME"></a>

## 152.62 `CONFIG_BMP180_OSR_RUNTIME`

**提示（Prompt）**：在运行时修改过采样率（OSR）

**说明（Help）**

允许运行时修改过采样值（Oversampling Value）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMP180 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmp180/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp180/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMP180 压力传感器（Pressure Sensor）

**配置项引用（Symbol References）**：[`CONFIG_BMP180`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMP180)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMP388"></a>

## 152.63 `CONFIG_BMP388`

**提示（Prompt）**：Bosch BMP388 压力传感器（Pressure Sensor）

**说明（Help）**

启用 Bosch BMP388 压力传感器（Pressure Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_BOSCH_BMP388_ENABLED || DT_HAS_BOSCH_BMP390_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n || n
CONFIG_SPI if n || n
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmp388/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp388/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_BMP388_ODR_RUNTIME"></a>

## 152.64 `CONFIG_BMP388_ODR_RUNTIME`

**提示（Prompt）**：在运行时修改输出数据速率（ODR）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMP388 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmp388/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp388/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMP388 压力传感器（Pressure Sensor）

**配置项引用（Symbol References）**：[`CONFIG_BMP388`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMP388)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMP388_OSR_RUNTIME"></a>

## 152.65 `CONFIG_BMP388_OSR_RUNTIME`

**提示（Prompt）**：在运行时修改过采样率（OSR）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMP388 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmp388/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp388/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMP388 压力传感器（Pressure Sensor）

**配置项引用（Symbol References）**：[`CONFIG_BMP388`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMP388)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMP388_THREAD_PRIORITY"></a>

## 152.66 `CONFIG_BMP388_THREAD_PRIORITY`

**提示（Prompt）**：专用线程优先级（Own Thread Priority）

**说明（Help）**

驱动用于处理中断的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMP388_TRIGGER_OWN_THREAD && CONFIG_BMP388 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmp388/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp388/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMP388 压力传感器（Pressure Sensor）

**配置项引用（Symbol References）**：[`CONFIG_BMP388_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMP388_TRIGGER_OWN_THREAD)、[`CONFIG_BMP388`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMP388)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMP388_THREAD_STACK_SIZE"></a>

## 152.67 `CONFIG_BMP388_THREAD_STACK_SIZE`

**提示（Prompt）**：专用线程栈大小（Own Thread Stack Size）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMP388_TRIGGER_OWN_THREAD && CONFIG_BMP388 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmp388/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp388/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMP388 压力传感器（Pressure Sensor）

**配置项引用（Symbol References）**：[`CONFIG_BMP388_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMP388_TRIGGER_OWN_THREAD)、[`CONFIG_BMP388`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMP388)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMP388_TRIGGER_DIRECT"></a>

## 152.68 `CONFIG_BMP388_TRIGGER_DIRECT`

**提示（Prompt）**：使用中断请求处理程序（IRQ Handler）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMP388_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmp388/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp388/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMP388 压力传感器（Pressure Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMP388_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMP388_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMP388_TRIGGER`。

<a id="CONFIG_BMP388_TRIGGER_GLOBAL_THREAD"></a>

## 152.69 `CONFIG_BMP388_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMP388_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmp388/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp388/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMP388 压力传感器（Pressure Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMP388_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMP388_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMP388_TRIGGER`。

<a id="CONFIG_BMP388_TRIGGER_MODE"></a>

## 152.70 `CONFIG_BMP388_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMP388 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_BMP388_TRIGGER_GLOBAL_THREAD
```

**可选项（Choices）**

```text
CONFIG_BMP388_TRIGGER_NONE
CONFIG_BMP388_TRIGGER_GLOBAL_THREAD
CONFIG_BMP388_TRIGGER_OWN_THREAD
CONFIG_BMP388_TRIGGER_DIRECT
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmp388/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp388/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMP388 压力传感器（Pressure Sensor）

**配置项引用（Symbol References）**：[`CONFIG_BMP388`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMP388)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_BMP388_TRIGGER_GLOBAL_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMP388_TRIGGER_GLOBAL_THREAD)、[`CONFIG_BMP388_TRIGGER_NONE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMP388_TRIGGER_NONE)、[`CONFIG_BMP388_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMP388_TRIGGER_OWN_THREAD)、[`CONFIG_BMP388_TRIGGER_DIRECT`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMP388_TRIGGER_DIRECT)。

<a id="CONFIG_BMP388_TRIGGER_NONE"></a>

## 152.71 `CONFIG_BMP388_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BMP388_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmp388/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp388/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMP388 压力传感器（Pressure Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMP388_TRIGGER_MODE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMP388_TRIGGER_MODE)。

<a id="CONFIG_BMP388_TRIGGER_OWN_THREAD"></a>

## 152.72 `CONFIG_BMP388_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMP388_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmp388/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp388/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMP388 压力传感器（Pressure Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMP388_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMP388_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMP388_TRIGGER`。

<a id="CONFIG_BMP581"></a>

## 152.73 `CONFIG_BMP581`

**提示（Prompt）**：BMP581 大气压力传感器（Barometric Pressure Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BOSCH_BMP581_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_I2C_RTIO if n
CONFIG_SPI if n
CONFIG_SPI_RTIO if n
CONFIG_I3C if n
CONFIG_I3C_RTIO if n
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmp581/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp581/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_I3C`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C)、[`CONFIG_I3C_RTIO`](P108_drivers_i3c_配置项参考.md#CONFIG_I3C_RTIO)。

<a id="CONFIG_BMP581_STREAM"></a>

## 152.74 `CONFIG_BMP581_STREAM`

**提示（Prompt）**：流式模式（Streaming Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmp581/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp581/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

<a id="CONFIG_BQ274XX"></a>

## 152.75 `CONFIG_BQ274XX`

**提示（Prompt）**：BQ274xx 电量计（Fuel Gauge）

**说明（Help）**

启用基于 I2C 的 BQ274xx 电量计（Fuel Gauge）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_BQ274XX_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/bq274xx/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/bq274xx/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_BQ274XX_PM"></a>

## 152.76 `CONFIG_BQ274XX_PM`

**提示（Prompt）**：BQ274XX 电源管理（Power Management）

**说明（Help）**

此选项启用 BQ274XX 的设备电源管理功能。注意：如果未使用 `int_gpios` 引脚，必须禁用此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE && CONFIG_BQ274XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/ti/bq274xx/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/bq274xx/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BQ274xx 电量计（Fuel Gauge）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)、[`CONFIG_BQ274XX`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BQ274XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BQ274XX_THREAD_PRIORITY"></a>

## 152.77 `CONFIG_BQ274XX_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BQ274XX_TRIGGER_OWN_THREAD && CONFIG_BQ274XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/ti/bq274xx/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/bq274xx/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BQ274xx 电量计（Fuel Gauge）

**配置项引用（Symbol References）**：[`CONFIG_BQ274XX_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BQ274XX_TRIGGER_OWN_THREAD)、[`CONFIG_BQ274XX`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BQ274XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BQ274XX_THREAD_STACK_SIZE"></a>

## 152.78 `CONFIG_BQ274XX_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BQ274XX_TRIGGER_OWN_THREAD && CONFIG_BQ274XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/ti/bq274xx/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/bq274xx/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BQ274xx 电量计（Fuel Gauge）

**配置项引用（Symbol References）**：[`CONFIG_BQ274XX_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BQ274XX_TRIGGER_OWN_THREAD)、[`CONFIG_BQ274XX`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BQ274XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BQ274XX_TRIGGER_GLOBAL_THREAD"></a>

## 152.79 `CONFIG_BQ274XX_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BQ274XX_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ti/bq274xx/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/bq274xx/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BQ274xx 电量计（Fuel Gauge） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BQ274XX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BQ274XX_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BQ274XX_TRIGGER`。

<a id="CONFIG_BQ274XX_TRIGGER_MODE"></a>

## 152.80 `CONFIG_BQ274XX_TRIGGER_MODE`

**提示（Prompt）**：触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BQ274XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_BQ274XX_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_BQ274XX_TRIGGER_NONE
CONFIG_BQ274XX_TRIGGER_GLOBAL_THREAD
CONFIG_BQ274XX_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/ti/bq274xx/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/bq274xx/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BQ274xx 电量计（Fuel Gauge）

**配置项引用（Symbol References）**：[`CONFIG_BQ274XX`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BQ274XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_BQ274XX_TRIGGER_NONE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BQ274XX_TRIGGER_NONE)、[`CONFIG_BQ274XX_TRIGGER_GLOBAL_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BQ274XX_TRIGGER_GLOBAL_THREAD)、[`CONFIG_BQ274XX_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BQ274XX_TRIGGER_OWN_THREAD)。

<a id="CONFIG_BQ274XX_TRIGGER_NONE"></a>

## 152.81 `CONFIG_BQ274XX_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BQ274XX_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/ti/bq274xx/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/bq274xx/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BQ274xx 电量计（Fuel Gauge） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BQ274XX_TRIGGER_MODE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BQ274XX_TRIGGER_MODE)。

<a id="CONFIG_BQ274XX_TRIGGER_OWN_THREAD"></a>

## 152.82 `CONFIG_BQ274XX_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BQ274XX_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ti/bq274xx/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/bq274xx/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BQ274xx 电量计（Fuel Gauge） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BQ274XX_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BQ274XX_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BQ274XX_TRIGGER`。

<a id="CONFIG_CCS811"></a>

## 152.83 `CONFIG_CCS811`

**提示（Prompt）**：CCS811 数字气体传感器（Digital Gas Sensor）

**说明（Help）**

启用 CCS811 气体传感器（Gas Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMS_CCS811_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ams/ccs811/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ccs811/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_CCS811_DRIVE_MODE"></a>

## 152.84 `CONFIG_CCS811_DRIVE_MODE`

**提示（Prompt）**：测量驱动模式（Measurement Drive Mode）

**说明（Help）**

指定驱动使用的测量速率（Measurement Rate）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CCS811 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_CCS811_DRIVE_MODE_1
```

**可选项（Choices）**

```text
CONFIG_CCS811_DRIVE_MODE_0
CONFIG_CCS811_DRIVE_MODE_1
CONFIG_CCS811_DRIVE_MODE_2
CONFIG_CCS811_DRIVE_MODE_3
CONFIG_CCS811_DRIVE_MODE_4
```

**定义位置（Location）**：[`drivers/sensor/ams/ccs811/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ccs811/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → CCS811 数字气体传感器（Digital Gas Sensor）

**配置项引用（Symbol References）**：[`CONFIG_CCS811`](P152_drivers_sensor_配置项参考_4.md#CONFIG_CCS811)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_CCS811_DRIVE_MODE_1`](P152_drivers_sensor_配置项参考_4.md#CONFIG_CCS811_DRIVE_MODE_1)、[`CONFIG_CCS811_DRIVE_MODE_0`](P152_drivers_sensor_配置项参考_4.md#CONFIG_CCS811_DRIVE_MODE_0)、[`CONFIG_CCS811_DRIVE_MODE_2`](P152_drivers_sensor_配置项参考_4.md#CONFIG_CCS811_DRIVE_MODE_2)、[`CONFIG_CCS811_DRIVE_MODE_3`](P152_drivers_sensor_配置项参考_4.md#CONFIG_CCS811_DRIVE_MODE_3)、[`CONFIG_CCS811_DRIVE_MODE_4`](P152_drivers_sensor_配置项参考_4.md#CONFIG_CCS811_DRIVE_MODE_4)。

<a id="CONFIG_CCS811_DRIVE_MODE_0"></a>

## 152.85 `CONFIG_CCS811_DRIVE_MODE_0`

**提示（Prompt）**：禁用测量（Measurements Disabled）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CCS811_DRIVE_MODE>
```

**定义位置（Location）**：[`drivers/sensor/ams/ccs811/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ccs811/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → CCS811 数字气体传感器（Digital Gas Sensor） → 测量驱动模式（Measurement Drive Mode）

**配置项引用（Symbol References）**：[`CONFIG_CCS811_DRIVE_MODE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_CCS811_DRIVE_MODE)。

<a id="CONFIG_CCS811_DRIVE_MODE_1"></a>

## 152.86 `CONFIG_CCS811_DRIVE_MODE_1`

**提示（Prompt）**：每秒测量一次

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CCS811_DRIVE_MODE>
```

**定义位置（Location）**：[`drivers/sensor/ams/ccs811/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ccs811/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → CCS811 数字气体传感器（Digital Gas Sensor） → 测量驱动模式（Measurement Drive Mode）

**配置项引用（Symbol References）**：[`CONFIG_CCS811_DRIVE_MODE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_CCS811_DRIVE_MODE)。

<a id="CONFIG_CCS811_DRIVE_MODE_2"></a>

## 152.87 `CONFIG_CCS811_DRIVE_MODE_2`

**提示（Prompt）**：每 10 秒测量一次

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CCS811_DRIVE_MODE>
```

**定义位置（Location）**：[`drivers/sensor/ams/ccs811/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ccs811/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → CCS811 数字气体传感器（Digital Gas Sensor） → 测量驱动模式（Measurement Drive Mode）

**配置项引用（Symbol References）**：[`CONFIG_CCS811_DRIVE_MODE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_CCS811_DRIVE_MODE)。

<a id="CONFIG_CCS811_DRIVE_MODE_3"></a>

## 152.88 `CONFIG_CCS811_DRIVE_MODE_3`

**提示（Prompt）**：每 60 秒测量一次

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CCS811_DRIVE_MODE>
```

**定义位置（Location）**：[`drivers/sensor/ams/ccs811/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ccs811/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → CCS811 数字气体传感器（Digital Gas Sensor） → 测量驱动模式（Measurement Drive Mode）

**配置项引用（Symbol References）**：[`CONFIG_CCS811_DRIVE_MODE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_CCS811_DRIVE_MODE)。

<a id="CONFIG_CCS811_DRIVE_MODE_4"></a>

## 152.89 `CONFIG_CCS811_DRIVE_MODE_4`

**提示（Prompt）**：每 250 毫秒测量一次

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CCS811_DRIVE_MODE>
```

**定义位置（Location）**：[`drivers/sensor/ams/ccs811/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ccs811/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → CCS811 数字气体传感器（Digital Gas Sensor） → 测量驱动模式（Measurement Drive Mode）

**配置项引用（Symbol References）**：[`CONFIG_CCS811_DRIVE_MODE`](P152_drivers_sensor_配置项参考_4.md#CONFIG_CCS811_DRIVE_MODE)。

<a id="CONFIG_CCS811_THREAD_PRIORITY"></a>

## 152.90 `CONFIG_CCS811_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CCS811_TRIGGER_OWN_THREAD && CONFIG_CCS811 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/ams/ccs811/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ccs811/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → CCS811 数字气体传感器（Digital Gas Sensor）

**配置项引用（Symbol References）**：[`CONFIG_CCS811_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_CCS811_TRIGGER_OWN_THREAD)、[`CONFIG_CCS811`](P152_drivers_sensor_配置项参考_4.md#CONFIG_CCS811)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_CCS811_THREAD_STACK_SIZE"></a>

## 152.91 `CONFIG_CCS811_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CCS811_TRIGGER_OWN_THREAD && CONFIG_CCS811 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/ams/ccs811/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ccs811/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → CCS811 数字气体传感器（Digital Gas Sensor）

**配置项引用（Symbol References）**：[`CONFIG_CCS811_TRIGGER_OWN_THREAD`](P152_drivers_sensor_配置项参考_4.md#CONFIG_CCS811_TRIGGER_OWN_THREAD)、[`CONFIG_CCS811`](P152_drivers_sensor_配置项参考_4.md#CONFIG_CCS811)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_CCS811_TRIGGER_GLOBAL_THREAD"></a>

## 152.92 `CONFIG_CCS811_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_CCS811_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ams/ccs811/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ccs811/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → CCS811 数字气体传感器（Digital Gas Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_CCS811_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CCS811_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CCS811_TRIGGER`。

<a id="CONFIG_CCS811_TRIGGER_NONE"></a>

## 152.93 `CONFIG_CCS811_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/ams/ccs811/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ccs811/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → CCS811 数字气体传感器（Digital Gas Sensor） → 触发模式（Trigger Mode）

<a id="CONFIG_CCS811_TRIGGER_OWN_THREAD"></a>

## 152.94 `CONFIG_CCS811_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_CCS811_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ams/ccs811/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ccs811/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → CCS811 数字气体传感器（Digital Gas Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_CCS811_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CCS811_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CCS811_TRIGGER`。

<a id="CONFIG_CHT8315"></a>

## 152.95 `CONFIG_CHT8315`

**提示（Prompt）**：Sensylink CHT8315 温湿度传感器（Temperature and Humidity Sensor）

**说明（Help）**

启用 Sensylink CHT8315 温湿度传感器（Temperature and Humidity Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SENSYLINK_CHT8315_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/cht8315/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/cht8315/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_CHT8315_TRIGGER"></a>

## 152.96 `CONFIG_CHT8315_TRIGGER`

**提示（Prompt）**：Sensylink CHT8315 触发器（Trigger）

**说明（Help）**

启用 CHT8315 基于中断的触发支持。要求传感器未设置为单次模式（One-shot Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/cht8315/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/cht8315/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

<a id="CONFIG_CURRENT_AMP"></a>

## 152.97 `CONFIG_CURRENT_AMP`

**提示（Prompt）**：电流检测放大器（Current Sense Amplifier）驱动

**说明（Help）**

启用电流检测放大器（Current Sense Amplifier）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CURRENT_SENSE_AMPLIFIER_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/sensor/current_amp/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/current_amp/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_D6F"></a>

## 152.98 `CONFIG_D6F`

**提示（Prompt）**：D6F 质量流量传感器（Mass Flow Rate Sensor）

**说明（Help）**

启用 Omron D6F 质量流量传感器（Mass Flow Rate Sensor）驱动。此系列传感器输出模拟电压，通过模数转换器（ADC）读取。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_OMRON_D6F_P0001_ENABLED || DT_HAS_OMRON_D6F_P0010_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
CONFIG_FPU if CONFIG_CPU_HAS_FPU
```

**定义位置（Location）**：[`drivers/sensor/omron/d6f/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/omron/d6f/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)、[`CONFIG_CPU_HAS_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_FPU)。

<a id="CONFIG_DHT"></a>

## 152.99 `CONFIG_DHT`

**提示（Prompt）**：DHT 温湿度传感器（Temperature and Humidity Sensor）

**说明（Help）**

启用 DHT 系列温湿度传感器（Temperature and Humidity Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AOSONG_DHT_ENABLED && CONFIG_GPIO && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/aosong/dht/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/aosong/dht/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_DHT20"></a>

## 152.100 `CONFIG_DHT20`

**提示（Prompt）**：DHT20 / AHT20 / AM2301B 温湿度传感器（Temperature and Humidity Sensor）

**说明（Help）**

启用 DHT20 / AHT20 / AM2301B 温湿度传感器（Temperature and Humidity Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_AOSONG_DHT20_ENABLED || DT_HAS_AOSONG_AHT20_ENABLED || DT_HAS_AOSONG_AM2301B_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/aosong/dht20/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/aosong/dht20/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<!-- kconfig-navigation -->

[上一章](P151_drivers_sensor_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P153_drivers_sensor_配置项参考_5.md)
