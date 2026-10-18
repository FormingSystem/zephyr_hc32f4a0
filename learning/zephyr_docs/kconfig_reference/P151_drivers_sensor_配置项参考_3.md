---
id: learning.zephyr-docs.kconfig-reference.page-151
title: "`drivers/sensor`配置项参考（3/15）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第151章\_`drivers/sensor`配置项参考（3/15）

本章翻译官方 Kconfig 数据库中 `drivers/sensor` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BME280_STANDBY_500MS"></a>

## 151.1 `CONFIG_BME280_STANDBY_500MS`

**提示（Prompt）**：500 ms

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 待机时间（Standby Time）

<a id="CONFIG_BME280_STANDBY_62MS"></a>

## 151.2 `CONFIG_BME280_STANDBY_62MS`

**提示（Prompt）**：62.5 ms

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 待机时间（Standby Time）

<a id="CONFIG_BME280_TEMP_OVER_16X"></a>

## 151.3 `CONFIG_BME280_TEMP_OVER_16X`

**提示（Prompt）**：16 倍（x16）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 温度过采样（Temperature Oversampling）

<a id="CONFIG_BME280_TEMP_OVER_1X"></a>

## 151.4 `CONFIG_BME280_TEMP_OVER_1X`

**提示（Prompt）**：1 倍（x1）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 温度过采样（Temperature Oversampling）

<a id="CONFIG_BME280_TEMP_OVER_2X"></a>

## 151.5 `CONFIG_BME280_TEMP_OVER_2X`

**提示（Prompt）**：2 倍（x2）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 温度过采样（Temperature Oversampling）

<a id="CONFIG_BME280_TEMP_OVER_4X"></a>

## 151.6 `CONFIG_BME280_TEMP_OVER_4X`

**提示（Prompt）**：4 倍（x4）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 温度过采样（Temperature Oversampling）

<a id="CONFIG_BME280_TEMP_OVER_8X"></a>

## 151.7 `CONFIG_BME280_TEMP_OVER_8X`

**提示（Prompt）**：8 倍（x8）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme280/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme280/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME280/BMP280 传感器 → BME280 温度过采样（Temperature Oversampling）

<a id="CONFIG_BME680"></a>

## 151.8 `CONFIG_BME680`

**提示（Prompt）**：BME680 传感器

**说明（Help）**

启用 BME680 基于 I²C 或 SPI 的温度、压力、湿度和气体传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BOSCH_BME680_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_RTIO_OP_DELAY if CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_RTIO_OP_DELAY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_OP_DELAY)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_BME680_FILTER_128"></a>

## 151.9 `CONFIG_BME680_FILTER_128`

**提示（Prompt）**：128

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 无限冲激响应（IIR）低通滤波器系数

<a id="CONFIG_BME680_FILTER_16"></a>

## 151.10 `CONFIG_BME680_FILTER_16`

**提示（Prompt）**：16

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 无限冲激响应（IIR）低通滤波器系数

<a id="CONFIG_BME680_FILTER_2"></a>

## 151.11 `CONFIG_BME680_FILTER_2`

**提示（Prompt）**：2

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 无限冲激响应（IIR）低通滤波器系数

<a id="CONFIG_BME680_FILTER_32"></a>

## 151.12 `CONFIG_BME680_FILTER_32`

**提示（Prompt）**：32

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 无限冲激响应（IIR）低通滤波器系数

<a id="CONFIG_BME680_FILTER_4"></a>

## 151.13 `CONFIG_BME680_FILTER_4`

**提示（Prompt）**：4

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 无限冲激响应（IIR）低通滤波器系数

<a id="CONFIG_BME680_FILTER_64"></a>

## 151.14 `CONFIG_BME680_FILTER_64`

**提示（Prompt）**：64

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 无限冲激响应（IIR）低通滤波器系数

<a id="CONFIG_BME680_FILTER_8"></a>

## 151.15 `CONFIG_BME680_FILTER_8`

**提示（Prompt）**：8

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 无限冲激响应（IIR）低通滤波器系数

<a id="CONFIG_BME680_FILTER_OFF"></a>

## 151.16 `CONFIG_BME680_FILTER_OFF`

**提示（Prompt）**：关闭滤波器（Filter Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 无限冲激响应（IIR）低通滤波器系数

<a id="CONFIG_BME680_HEATR_DUR_LP"></a>

## 151.17 `CONFIG_BME680_HEATR_DUR_LP`

**提示（Prompt）**：197

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 气体传感器加热持续时间，单位为毫秒

<a id="CONFIG_BME680_HEATR_DUR_ULP"></a>

## 151.18 `CONFIG_BME680_HEATR_DUR_ULP`

**提示（Prompt）**：1943

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 气体传感器加热持续时间，单位为毫秒

<a id="CONFIG_BME680_HEATR_TEMP_LP"></a>

## 151.19 `CONFIG_BME680_HEATR_TEMP_LP`

**提示（Prompt）**：320

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 气体传感器加热器温度，单位为摄氏度

<a id="CONFIG_BME680_HEATR_TEMP_ULP"></a>

## 151.20 `CONFIG_BME680_HEATR_TEMP_ULP`

**提示（Prompt）**：400

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 气体传感器加热器温度，单位为摄氏度

<a id="CONFIG_BME680_HUMIDITY_OVER_16X"></a>

## 151.21 `CONFIG_BME680_HUMIDITY_OVER_16X`

**提示（Prompt）**：16 倍（x16）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 湿度过采样

<a id="CONFIG_BME680_HUMIDITY_OVER_1X"></a>

## 151.22 `CONFIG_BME680_HUMIDITY_OVER_1X`

**提示（Prompt）**：1 倍（x1）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 湿度过采样

<a id="CONFIG_BME680_HUMIDITY_OVER_2X"></a>

## 151.23 `CONFIG_BME680_HUMIDITY_OVER_2X`

**提示（Prompt）**：2 倍（x2）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 湿度过采样

<a id="CONFIG_BME680_HUMIDITY_OVER_4X"></a>

## 151.24 `CONFIG_BME680_HUMIDITY_OVER_4X`

**提示（Prompt）**：4 倍（x4）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 湿度过采样

<a id="CONFIG_BME680_HUMIDITY_OVER_8X"></a>

## 151.25 `CONFIG_BME680_HUMIDITY_OVER_8X`

**提示（Prompt）**：8 倍（x8）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 湿度过采样

<a id="CONFIG_BME680_PRESS_OVER_16X"></a>

## 151.26 `CONFIG_BME680_PRESS_OVER_16X`

**提示（Prompt）**：16 倍（x16）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 压力过采样

<a id="CONFIG_BME680_PRESS_OVER_1X"></a>

## 151.27 `CONFIG_BME680_PRESS_OVER_1X`

**提示（Prompt）**：1 倍（x1）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 压力过采样

<a id="CONFIG_BME680_PRESS_OVER_2X"></a>

## 151.28 `CONFIG_BME680_PRESS_OVER_2X`

**提示（Prompt）**：2 倍（x2）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 压力过采样

<a id="CONFIG_BME680_PRESS_OVER_4X"></a>

## 151.29 `CONFIG_BME680_PRESS_OVER_4X`

**提示（Prompt）**：4 倍（x4）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 压力过采样

<a id="CONFIG_BME680_PRESS_OVER_8X"></a>

## 151.30 `CONFIG_BME680_PRESS_OVER_8X`

**提示（Prompt）**：8 倍（x8）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 压力过采样

<a id="CONFIG_BME680_TEMP_OVER_16X"></a>

## 151.31 `CONFIG_BME680_TEMP_OVER_16X`

**提示（Prompt）**：16 倍（x16）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 温度过采样

<a id="CONFIG_BME680_TEMP_OVER_1X"></a>

## 151.32 `CONFIG_BME680_TEMP_OVER_1X`

**提示（Prompt）**：1 倍（x1）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 温度过采样

<a id="CONFIG_BME680_TEMP_OVER_2X"></a>

## 151.33 `CONFIG_BME680_TEMP_OVER_2X`

**提示（Prompt）**：2 倍（x2）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 温度过采样

<a id="CONFIG_BME680_TEMP_OVER_4X"></a>

## 151.34 `CONFIG_BME680_TEMP_OVER_4X`

**提示（Prompt）**：4 倍（x4）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 温度过采样

<a id="CONFIG_BME680_TEMP_OVER_8X"></a>

## 151.35 `CONFIG_BME680_TEMP_OVER_8X`

**提示（Prompt）**：8 倍（x8）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bme680/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bme680/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BME680 传感器 → BME680 温度过采样

<a id="CONFIG_BMG160"></a>

## 151.36 `CONFIG_BMG160`

**提示（Prompt）**：Bosch BMG160 陀螺仪（Gyroscope）支持

**说明（Help）**

启用 Bosch BMG160 陀螺仪支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BOSCH_BMG160_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_BMG160_I2C_SPEED_FAST"></a>

## 151.37 `CONFIG_BMG160_I2C_SPEED_FAST`

**提示（Prompt）**：快速模式（Fast）

**说明（Help）**

最高 400 kHz 的快速总线速率（Fast Bus Speed）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → BMG160 I²C 总线速度

<a id="CONFIG_BMG160_I2C_SPEED_STANDARD"></a>

## 151.38 `CONFIG_BMG160_I2C_SPEED_STANDARD`

**提示（Prompt）**：标准模式（Standard）

**说明（Help）**

最高 100 kHz 的标准总线速度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → BMG160 I²C 总线速度

<a id="CONFIG_BMG160_ODR_100"></a>

## 151.39 `CONFIG_BMG160_ODR_100`

**提示（Prompt）**：频率：100 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → 陀螺仪采样频率（Sampling Frequency）。

<a id="CONFIG_BMG160_ODR_1000"></a>

## 151.40 `CONFIG_BMG160_ODR_1000`

**提示（Prompt）**：1000 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → 陀螺仪采样频率（Sampling Frequency）。

<a id="CONFIG_BMG160_ODR_200"></a>

## 151.41 `CONFIG_BMG160_ODR_200`

**提示（Prompt）**：频率：200 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → 陀螺仪采样频率（Sampling Frequency）。

<a id="CONFIG_BMG160_ODR_2000"></a>

## 151.42 `CONFIG_BMG160_ODR_2000`

**提示（Prompt）**：2000 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → 陀螺仪采样频率（Sampling Frequency）。

<a id="CONFIG_BMG160_ODR_400"></a>

## 151.43 `CONFIG_BMG160_ODR_400`

**提示（Prompt）**：频率：400 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → 陀螺仪采样频率（Sampling Frequency）。

<a id="CONFIG_BMG160_ODR_RUNTIME"></a>

## 151.44 `CONFIG_BMG160_ODR_RUNTIME`

**提示（Prompt）**：在运行时设置（Set at Runtime）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → 陀螺仪采样频率（Sampling Frequency）。

<a id="CONFIG_BMG160_RANGE_1000DPS"></a>

## 151.45 `CONFIG_BMG160_RANGE_1000DPS`

**提示（Prompt）**：1000 度／秒（DPS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → 陀螺仪量程设置（Range Setting）。

<a id="CONFIG_BMG160_RANGE_125DPS"></a>

## 151.46 `CONFIG_BMG160_RANGE_125DPS`

**提示（Prompt）**：125 度／秒（DPS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → 陀螺仪量程设置（Range Setting）。

<a id="CONFIG_BMG160_RANGE_2000DPS"></a>

## 151.47 `CONFIG_BMG160_RANGE_2000DPS`

**提示（Prompt）**：2000 度／秒（DPS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → 陀螺仪量程设置（Range Setting）。

<a id="CONFIG_BMG160_RANGE_250DPS"></a>

## 151.48 `CONFIG_BMG160_RANGE_250DPS`

**提示（Prompt）**：250 度／秒（DPS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → 陀螺仪量程设置（Range Setting）。

<a id="CONFIG_BMG160_RANGE_500DPS"></a>

## 151.49 `CONFIG_BMG160_RANGE_500DPS`

**提示（Prompt）**：500 度／秒（DPS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → 陀螺仪量程设置（Range Setting）。

<a id="CONFIG_BMG160_RANGE_RUNTIME"></a>

## 151.50 `CONFIG_BMG160_RANGE_RUNTIME`

**提示（Prompt）**：在运行时设置（Set at Runtime）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → 陀螺仪量程设置（Range Setting）。

<a id="CONFIG_BMG160_THREAD_PRIORITY"></a>

## 151.51 `CONFIG_BMG160_THREAD_PRIORITY`

**提示（Prompt）**：专用线程优先级（Own Thread Priority）

**说明（Help）**

处理中断的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMG160_TRIGGER_OWN_THREAD && CONFIG_BMG160 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持

**配置项引用（Symbol References）**：[`CONFIG_BMG160_TRIGGER_OWN_THREAD`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMG160_TRIGGER_OWN_THREAD)、[`CONFIG_BMG160`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMG160)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMG160_THREAD_STACK_SIZE"></a>

## 151.52 `CONFIG_BMG160_THREAD_STACK_SIZE`

**提示（Prompt）**：专用线程栈大小（Own Thread Stack Size）

**说明（Help）**

线程栈（Thread Stack）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMG160_TRIGGER_OWN_THREAD && CONFIG_BMG160 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持

**配置项引用（Symbol References）**：[`CONFIG_BMG160_TRIGGER_OWN_THREAD`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMG160_TRIGGER_OWN_THREAD)、[`CONFIG_BMG160`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMG160)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMG160_TRIGGER_GLOBAL_THREAD"></a>

## 151.53 `CONFIG_BMG160_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMG160_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMG160_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMG160_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMG160_TRIGGER`。

<a id="CONFIG_BMG160_TRIGGER_NONE"></a>

## 151.54 `CONFIG_BMG160_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → 触发模式（Trigger Mode）

<a id="CONFIG_BMG160_TRIGGER_OWN_THREAD"></a>

## 151.55 `CONFIG_BMG160_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMG160_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmg160/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmg160/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMG160 陀螺仪（Gyroscope）支持 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMG160_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMG160_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMG160_TRIGGER`。

<a id="CONFIG_BMI08X"></a>

## 151.56 `CONFIG_BMI08X`

**提示（Prompt）**：Bosch BMI08X 惯性测量单元（IMU）

**说明（Help）**

启用 Bosch BMI08X 惯性测量单元，提供加速度与角速率测量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_BOSCH_BMI08X_ACCEL_ENABLED || DT_HAS_BOSCH_BMI08X_GYRO_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n || n
CONFIG_SPI if n || n
CONFIG_SPI_RTIO if CONFIG_SPI
CONFIG_I2C_RTIO if CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)。

<a id="CONFIG_BMI08X_ACCEL_STREAM"></a>

## 151.57 `CONFIG_BMI08X_ACCEL_STREAM`

**提示（Prompt）**：加速度计流式模式（Streaming Mode，FIFO）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI08X 惯性测量单元（IMU）

<a id="CONFIG_BMI08X_ACCEL_THREAD_PRIORITY"></a>

## 151.58 `CONFIG_BMI08X_ACCEL_THREAD_PRIORITY`

**提示（Prompt）**：加速度计专用线程优先级

**说明（Help）**

处理中断的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI08X_ACCEL_TRIGGER_OWN_THREAD && CONFIG_BMI08X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI08X 惯性测量单元（IMU）

**配置项引用（Symbol References）**：[`CONFIG_BMI08X_ACCEL_TRIGGER_OWN_THREAD`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X_ACCEL_TRIGGER_OWN_THREAD)、[`CONFIG_BMI08X`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI08X_ACCEL_THREAD_STACK_SIZE"></a>

## 151.59 `CONFIG_BMI08X_ACCEL_THREAD_STACK_SIZE`

**提示（Prompt）**：加速度计专用线程栈大小

**说明（Help）**

线程栈（Thread Stack）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI08X_ACCEL_TRIGGER_OWN_THREAD && CONFIG_BMI08X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1536
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI08X 惯性测量单元（IMU）

**配置项引用（Symbol References）**：[`CONFIG_BMI08X_ACCEL_TRIGGER_OWN_THREAD`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X_ACCEL_TRIGGER_OWN_THREAD)、[`CONFIG_BMI08X`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI08X_ACCEL_TRIGGER_GLOBAL_THREAD"></a>

## 151.60 `CONFIG_BMI08X_ACCEL_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMI08X_ACCEL_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI08X 惯性测量单元（IMU） → 加速度计触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMI08X_ACCEL_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMI08X_ACCEL_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMI08X_ACCEL_TRIGGER`。

<a id="CONFIG_BMI08X_ACCEL_TRIGGER_MODE"></a>

## 151.61 `CONFIG_BMI08X_ACCEL_TRIGGER_MODE`

**提示（Prompt）**：加速度计触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI08X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_BMI08X_ACCEL_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_BMI08X_ACCEL_TRIGGER_NONE
CONFIG_BMI08X_ACCEL_TRIGGER_GLOBAL_THREAD
CONFIG_BMI08X_ACCEL_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI08X 惯性测量单元（IMU）

**配置项引用（Symbol References）**：[`CONFIG_BMI08X`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_BMI08X_ACCEL_TRIGGER_NONE`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X_ACCEL_TRIGGER_NONE)、[`CONFIG_BMI08X_ACCEL_TRIGGER_GLOBAL_THREAD`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X_ACCEL_TRIGGER_GLOBAL_THREAD)、[`CONFIG_BMI08X_ACCEL_TRIGGER_OWN_THREAD`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X_ACCEL_TRIGGER_OWN_THREAD)。

<a id="CONFIG_BMI08X_ACCEL_TRIGGER_NONE"></a>

## 151.62 `CONFIG_BMI08X_ACCEL_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BMI08X_ACCEL_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI08X 惯性测量单元（IMU） → 加速度计触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMI08X_ACCEL_TRIGGER_MODE`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X_ACCEL_TRIGGER_MODE)。

<a id="CONFIG_BMI08X_ACCEL_TRIGGER_OWN_THREAD"></a>

## 151.63 `CONFIG_BMI08X_ACCEL_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_BMI08X_ACCEL_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI08X 惯性测量单元（IMU） → 加速度计触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMI08X_ACCEL_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMI08X_ACCEL_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMI08X_ACCEL_TRIGGER`。

<a id="CONFIG_BMI08X_GYRO_STREAM"></a>

## 151.64 `CONFIG_BMI08X_GYRO_STREAM`

**提示（Prompt）**：陀螺仪流式模式（Streaming Mode，FIFO）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI08X 惯性测量单元（IMU）

<a id="CONFIG_BMI08X_GYRO_THREAD_PRIORITY"></a>

## 151.65 `CONFIG_BMI08X_GYRO_THREAD_PRIORITY`

**提示（Prompt）**：专用线程优先级（Own Thread Priority）

**说明（Help）**

处理中断的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI08X_GYRO_TRIGGER_OWN_THREAD && CONFIG_BMI08X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI08X 惯性测量单元（IMU）

**配置项引用（Symbol References）**：[`CONFIG_BMI08X_GYRO_TRIGGER_OWN_THREAD`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X_GYRO_TRIGGER_OWN_THREAD)、[`CONFIG_BMI08X`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI08X_GYRO_THREAD_STACK_SIZE"></a>

## 151.66 `CONFIG_BMI08X_GYRO_THREAD_STACK_SIZE`

**提示（Prompt）**：专用线程栈大小（Own Thread Stack Size）

**说明（Help）**

线程栈（Thread Stack）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI08X_GYRO_TRIGGER_OWN_THREAD && CONFIG_BMI08X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1536
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI08X 惯性测量单元（IMU）

**配置项引用（Symbol References）**：[`CONFIG_BMI08X_GYRO_TRIGGER_OWN_THREAD`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X_GYRO_TRIGGER_OWN_THREAD)、[`CONFIG_BMI08X`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI08X_GYRO_TRIGGER_GLOBAL_THREAD"></a>

## 151.67 `CONFIG_BMI08X_GYRO_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BMI08X_GYRO_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_BMI08X_GYRO_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI08X 惯性测量单元（IMU） → 陀螺仪触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMI08X_GYRO_TRIGGER_MODE`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X_GYRO_TRIGGER_MODE)、[`CONFIG_BMI08X_GYRO_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMI08X_GYRO_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMI08X_GYRO_TRIGGER`。

<a id="CONFIG_BMI08X_GYRO_TRIGGER_MODE"></a>

## 151.68 `CONFIG_BMI08X_GYRO_TRIGGER_MODE`

**提示（Prompt）**：陀螺仪触发模式（Trigger Mode）

**说明（Help）**

指定驱动使用的触发类型（Triggering Type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI08X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_BMI08X_GYRO_TRIGGER_NONE
```

**可选项（Choices）**

```text
CONFIG_BMI08X_GYRO_TRIGGER_NONE
CONFIG_BMI08X_GYRO_TRIGGER_GLOBAL_THREAD
CONFIG_BMI08X_GYRO_TRIGGER_OWN_THREAD
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI08X 惯性测量单元（IMU）

**配置项引用（Symbol References）**：[`CONFIG_BMI08X`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_BMI08X_GYRO_TRIGGER_NONE`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X_GYRO_TRIGGER_NONE)、[`CONFIG_BMI08X_GYRO_TRIGGER_GLOBAL_THREAD`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X_GYRO_TRIGGER_GLOBAL_THREAD)、[`CONFIG_BMI08X_GYRO_TRIGGER_OWN_THREAD`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X_GYRO_TRIGGER_OWN_THREAD)。

<a id="CONFIG_BMI08X_GYRO_TRIGGER_NONE"></a>

## 151.69 `CONFIG_BMI08X_GYRO_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BMI08X_GYRO_TRIGGER_MODE>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI08X 惯性测量单元（IMU） → 陀螺仪触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMI08X_GYRO_TRIGGER_MODE`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X_GYRO_TRIGGER_MODE)。

<a id="CONFIG_BMI08X_GYRO_TRIGGER_OWN_THREAD"></a>

## 151.70 `CONFIG_BMI08X_GYRO_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BMI08X_GYRO_TRIGGER_MODE>
```

**主动选择（Selects）**

```text
CONFIG_BMI08X_GYRO_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI08X 惯性测量单元（IMU） → 陀螺仪触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_BMI08X_GYRO_TRIGGER_MODE`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X_GYRO_TRIGGER_MODE)、[`CONFIG_BMI08X_GYRO_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMI08X_GYRO_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BMI08X_GYRO_TRIGGER`。

<a id="CONFIG_BMI08X_I2C_WRITE_BURST_SIZE"></a>

## 151.71 `CONFIG_BMI08X_I2C_WRITE_BURST_SIZE`

**提示（Prompt）**：单次 I²C 写入最大长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI08X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi08x/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI08X 惯性测量单元（IMU）

**配置项引用（Symbol References）**：[`CONFIG_BMI08X`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_BMI160"></a>

## 151.72 `CONFIG_BMI160`

**提示（Prompt）**：Bosch BMI160 惯性测量单元（IMU）

**说明（Help）**

启用 Bosch BMI160 惯性测量单元，提供加速度与角速率测量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BOSCH_BMI160_ENABLED && CONFIG_SENSOR
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

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_BMI160_ACCEL_ODR_100"></a>

## 151.73 `CONFIG_BMI160_ACCEL_ODR_100`

**提示（Prompt）**：频率：100 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_ACCEL_ODR_1600"></a>

## 151.74 `CONFIG_BMI160_ACCEL_ODR_1600`

**提示（Prompt）**：频率：1600 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_ACCEL_ODR_200"></a>

## 151.75 `CONFIG_BMI160_ACCEL_ODR_200`

**提示（Prompt）**：频率：200 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_ACCEL_ODR_25"></a>

## 151.76 `CONFIG_BMI160_ACCEL_ODR_25`

**提示（Prompt）**：频率：25 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_ACCEL_ODR_25_16"></a>

## 151.77 `CONFIG_BMI160_ACCEL_ODR_25_16`

**提示（Prompt）**：1.56 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI160_ACCEL_PMU_LOW_POWER && <choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计采样频率（Sampling Frequency）。

**配置项引用（Symbol References）**：[`CONFIG_BMI160_ACCEL_PMU_LOW_POWER`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI160_ACCEL_PMU_LOW_POWER)。

<a id="CONFIG_BMI160_ACCEL_ODR_25_2"></a>

## 151.78 `CONFIG_BMI160_ACCEL_ODR_25_2`

**提示（Prompt）**：频率：12.5 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_ACCEL_ODR_25_32"></a>

## 151.79 `CONFIG_BMI160_ACCEL_ODR_25_32`

**提示（Prompt）**：0.78 Hz

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI160_ACCEL_PMU_LOW_POWER && <choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计采样频率（Sampling Frequency）。

**配置项引用（Symbol References）**：[`CONFIG_BMI160_ACCEL_PMU_LOW_POWER`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI160_ACCEL_PMU_LOW_POWER)。

<a id="CONFIG_BMI160_ACCEL_ODR_25_4"></a>

## 151.80 `CONFIG_BMI160_ACCEL_ODR_25_4`

**提示（Prompt）**：频率：6.25 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI160_ACCEL_PMU_LOW_POWER && <choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计采样频率（Sampling Frequency）。

**配置项引用（Symbol References）**：[`CONFIG_BMI160_ACCEL_PMU_LOW_POWER`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI160_ACCEL_PMU_LOW_POWER)。

<a id="CONFIG_BMI160_ACCEL_ODR_25_8"></a>

## 151.81 `CONFIG_BMI160_ACCEL_ODR_25_8`

**提示（Prompt）**：频率（Frequency）：3.125 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMI160_ACCEL_PMU_LOW_POWER && <choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计采样频率（Sampling Frequency）。

**配置项引用（Symbol References）**：[`CONFIG_BMI160_ACCEL_PMU_LOW_POWER`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI160_ACCEL_PMU_LOW_POWER)。

<a id="CONFIG_BMI160_ACCEL_ODR_400"></a>

## 151.82 `CONFIG_BMI160_ACCEL_ODR_400`

**提示（Prompt）**：频率：400 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_ACCEL_ODR_50"></a>

## 151.83 `CONFIG_BMI160_ACCEL_ODR_50`

**提示（Prompt）**：频率：50 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_ACCEL_ODR_800"></a>

## 151.84 `CONFIG_BMI160_ACCEL_ODR_800`

**提示（Prompt）**：频率：800 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_ACCEL_ODR_RUNTIME"></a>

## 151.85 `CONFIG_BMI160_ACCEL_ODR_RUNTIME`

**提示（Prompt）**：在运行时设置（Set at Runtime）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_ACCEL_PMU_LOW_POWER"></a>

## 151.86 `CONFIG_BMI160_ACCEL_PMU_LOW_POWER`

**提示（Prompt）**：低功耗（Low Power）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计电源模式（Power Mode）

<a id="CONFIG_BMI160_ACCEL_PMU_NORMAL"></a>

## 151.87 `CONFIG_BMI160_ACCEL_PMU_NORMAL`

**提示（Prompt）**：正常（Normal）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计电源模式（Power Mode）

<a id="CONFIG_BMI160_ACCEL_PMU_RUNTIME"></a>

## 151.88 `CONFIG_BMI160_ACCEL_PMU_RUNTIME`

**提示（Prompt）**：在运行时设置（Set at Runtime）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计电源模式（Power Mode）

<a id="CONFIG_BMI160_ACCEL_PMU_SUSPEND"></a>

## 151.89 `CONFIG_BMI160_ACCEL_PMU_SUSPEND`

**提示（Prompt）**：挂起／不使用（Suspended/Not Used）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计电源模式（Power Mode）

<a id="CONFIG_BMI160_ACCEL_RANGE_16G"></a>

## 151.90 `CONFIG_BMI160_ACCEL_RANGE_16G`

**提示（Prompt）**：16G

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计量程设置（Range Setting）

<a id="CONFIG_BMI160_ACCEL_RANGE_2G"></a>

## 151.91 `CONFIG_BMI160_ACCEL_RANGE_2G`

**提示（Prompt）**：第二代移动通信（2G）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计量程设置（Range Setting）

<a id="CONFIG_BMI160_ACCEL_RANGE_4G"></a>

## 151.92 `CONFIG_BMI160_ACCEL_RANGE_4G`

**提示（Prompt）**：第四代移动通信（4G）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计量程设置（Range Setting）

<a id="CONFIG_BMI160_ACCEL_RANGE_8G"></a>

## 151.93 `CONFIG_BMI160_ACCEL_RANGE_8G`

**提示（Prompt）**：8G

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计量程设置（Range Setting）

<a id="CONFIG_BMI160_ACCEL_RANGE_RUNTIME"></a>

## 151.94 `CONFIG_BMI160_ACCEL_RANGE_RUNTIME`

**提示（Prompt）**：在运行时设置（Set at Runtime）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 加速度计量程设置（Range Setting）

<a id="CONFIG_BMI160_GYRO_ODR_100"></a>

## 151.95 `CONFIG_BMI160_GYRO_ODR_100`

**提示（Prompt）**：频率：100 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:199`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L199)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_GYRO_ODR_1600"></a>

## 151.96 `CONFIG_BMI160_GYRO_ODR_1600`

**提示（Prompt）**：频率：1600 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_GYRO_ODR_200"></a>

## 151.97 `CONFIG_BMI160_GYRO_ODR_200`

**提示（Prompt）**：频率：200 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_GYRO_ODR_25"></a>

## 151.98 `CONFIG_BMI160_GYRO_ODR_25`

**提示（Prompt）**：频率：25 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_GYRO_ODR_3200"></a>

## 151.99 `CONFIG_BMI160_GYRO_ODR_3200`

**提示（Prompt）**：频率：3200 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:214`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L214)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪采样频率（Sampling Frequency）。

<a id="CONFIG_BMI160_GYRO_ODR_400"></a>

## 151.100 `CONFIG_BMI160_GYRO_ODR_400`

**提示（Prompt）**：频率：400 Hz。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:205`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L205)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU） → 陀螺仪采样频率（Sampling Frequency）。

<!-- kconfig-navigation -->

[上一章](P150_drivers_sensor_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P152_drivers_sensor_配置项参考_4.md)
